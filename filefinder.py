from asyncore import write
import os
from importlib.resources import path
import json
import hashlib


def readPaths(dataPath):
    f = open(dataPath, 'r')
    data = json.load(f)
    f.close()
    return data


def isMD(dataPath):
    if(dataPath[-3:] == (".md")):
        return True
    else:
        return False


def genHASH(file):
    BLOCK_SIZE = 65536  # The size of each read from the file

    # Create the hash object, can use something other than `.sha256()` if you wish
    file_hash = hashlib.sha256()
    with open(file, 'rb') as f:  # Open the file to read it's bytes
        # Read from the file. Take in the amount declared above
        fb = f.read(BLOCK_SIZE)
        while len(fb) > 0:  # While there is still data being read from the file
            file_hash.update(fb)  # Update the hash
            fb = f.read(BLOCK_SIZE)  # Read the next block from the file

    # print(file_hash.hexdigest())  # Get the hexadecimal digest of the hash
    return file_hash.hexdigest()


def writeData(dataPath, data):
    f = open(dataPath, "w")
    f.write(json.dumps(data))
    f.close


# TODOS:
# write a log file
# add a converter
# add a path exists functions which checks if the entry is still valid


def isDocumented(dataPath, entry):
    data = readPaths(dataPath)
    if entry in data["path"]:
        id = data["path"].index(entry)
        time = os.path.getmtime(entry)
        if data["md"][id] and data["hash"][id] == genHASH(entry):
            print(entry + " | hat sich nicht verändert")
        elif data["md"][id]:
            data["hash"][id] = genHASH(entry)
            print(entry + " | hat sich seit dem letzten mal verändert")
        else:
            print(entry+" | ist nicht von bedeutung")
    else:
        time = os.path.getmtime(entry)
        data["path"].append(entry)
        data["md"].append(isMD(entry))
        if(isMD(entry)):
            data["hash"].append(genHASH(entry))
        else:
            data["hash"].append("no hash needed")
        print(entry+" | wurde hinzugefügt")
    writeData(dataPath, data)


# =================main========================
stdpath=r"C:\Users\Michael Obernhumer\Documents\Repository\bericht_converter"
start = stdpath+"\l1dir1"
dataPath = stdpath+"\data.json"
logpath=stdpath+"\log.txt"

dirList = ["IV"]
while(True):
    dirList.pop(len(dirList)-1)
    entries = os.listdir(start)
    for entry in entries:
        entry = start + "\\" + entry
        isDocumented(dataPath, entry)
        if os.path.isdir(entry):
            dirList.append(entry)
    if len(dirList) == 0:
        break
    start = dirList[len(dirList) - 1]
