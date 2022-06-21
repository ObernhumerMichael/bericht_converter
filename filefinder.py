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


def writePath(dataPath, data, path):
    f = open(dataPath, "w")
    data["path"].append(path)
    output = json.dumps(data)
    f.write(output)
    f.close


def writeTime(dataPath, data, time):
    f = open(dataPath, "w")
    data["time"].append(time)
    output = json.dumps(data)
    f.write(output)
    f.close


def isMD(dataPath):
    if(dataPath[-3:] == (".md")):
        return True
    else:
        return False


def writeMD(dataPath, data, status):
    f = open(dataPath, "w")
    data["md"].append(status)
    output = json.dumps(data)
    f.write(output)
    f.close


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


def writeHASH(dataPath, data, hash):
    f = open(dataPath, "w")
    data["hash"].append(hash)
    output = json.dumps(data)
    f.write(output)
    f.close

# TODOS: 
# Replace modification check using time with hash check
# perform everyithing in a dict and write everyting at once
# add a converter
# add a path exists functions which checks if the entry is still valid
# write a log file


def isDocumented(dataPath, entry):
    data = readPaths(dataPath)
    if entry in data["path"]:
        id = data["path"].index(entry)
        time = os.path.getmtime(entry)
        if data["time"][id] != time:  # Erweitern mit HASH
            # Note: Hier verknüpfung zu Converter bauen
            data["time"][id] = time
            print(entry + " | hat sich seit dem letzten mal verändert")
        else:
            print(entry + " | hat sich nicht verändert")
    else:
        time = os.path.getmtime(entry)
        writePath(dataPath, data, entry)
        writeTime(dataPath, data, time)
        writeMD(dataPath, data, isMD(entry))
        if(isMD(entry)):
            writeHASH(dataPath, data,genHASH(entry))
        else:
            writeHASH(dataPath,data,"no hash needed")
        print(entry+" | wurde hinzugefügt")


# =================main========================
start = r"C:\Users\Michael Obernhumer\Documents\prgoramms_selfmade\Skripts\file-finder\l1dir1"
dataPath = r"C:\Users\Michael Obernhumer\Documents\prgoramms_selfmade\Skripts\file-finder\data.json"

time = os.path.getmtime(start)
print(time)


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
