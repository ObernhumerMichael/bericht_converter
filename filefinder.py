import asyncio
import os
from importlib.resources import path
import json
import hashlib
import re


def readData(dataPath):
    f = open(dataPath, 'r')
    data = json.load(f)
    f.close()
    return data


def writeData(dataPath, data):
    f = open(dataPath, "w")
    f.write(json.dumps(data))
    f.close

    
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

    return file_hash.hexdigest()


def writeLog(logPath, log):
    f = open(logPath, 'r')
    fullLog = f.read()
    f.close()

    fullLog = fullLog+'\n'+log

    f = open(logPath, "w")
    f.write(fullLog)
    f.close

def clearLog(logPath):
    f = open(logPath, 'w')
    f.write("")
    f.close()

def readMD(path):
    f = open(path, "r")
    content = f.read()
    f.close()
    return content


def convert(filePath, stylePath, logPath):
    # gets the Paths
    content = readMD(stylePath)+"\n"+readMD(filePath)
    match = re.search(r"(.*\\)", filePath)
    tempPath = match.group(1)
    tempPath = tempPath+"temp.md"
    pdfPath = tempPath[:-2]+"pdf"

    f = open(tempPath, "w")
    f.write(content)
    f.close()

    writeLog(logPath, "temp.md for " + filePath+" has been created")
    os.system('md2pdf "' + tempPath+'"')

    if os.path.exists(pdfPath):
        writeLog(logPath, "File has been succesfully converted :"+tempPath)
    else:
        writeLog(logPath, "temp.md couldn't be converted"+tempPath)
    os.remove(tempPath)
    os.rename(pdfPath, filePath[:-2]+"pdf")



# =================main========================
stdpath = r"C:\Users\Michael Obernhumer\Documents\Repository\bericht_converter"
start = stdpath+"\l1dir1"
dataPath = stdpath+"\data.json"
logPath = stdpath+"\log.txt"
stylePath = stdpath+"\style.txt"
clearLog(logPath)

dirList = ["IV"]
while(True):
    dirList.pop(len(dirList)-1)
    entries = os.listdir(start)
    for entry in entries:
        entry = start + "\\" + entry
        data = readData(dataPath)
        if entry in data["path"]:
            id = data["path"].index(entry)
            if data["md"][id] and data["hash"][id] == genHASH(entry):
                writeLog(logPath, entry + " | hasn't changed")
            elif data["md"][id]:
                data["hash"][id] = genHASH(entry)
                # build interface to converter here
                convert(entry, stylePath, logPath)
                writeLog(logPath, entry + " | has changed since the last time")
            else:
                writeLog(logPath, entry+" | isn't relevant")
        else:
            data["path"].append(entry)
            data["md"].append(isMD(entry))
            if(isMD(entry)):
                data["hash"].append(genHASH(entry))
                convert(entry, stylePath, logPath)
            else:
                data["hash"].append("no hash needed")
            writeLog(logPath, entry+" | was appended")
        writeData(dataPath, data)

        if os.path.isdir(entry):
            dirList.append(entry)
    if len(dirList) == 0:
        break
    start = dirList[len(dirList) - 1]
