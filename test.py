import asyncio
import os
from importlib.resources import path
import json
import hashlib
import re
def readMD(path):
    f=open(path,"r")
    content=f.read()
    f.close()
    return content

def convert(filePath,stylePath):
    content=readMD(stylePath)+"\n"+readMD(filePath)
    match=re.search(r"(.*\\)",filePath)
    tempPath=match.group(1)
    tempPath=tempPath+"temp.md"
    print(tempPath)
    f=open(tempPath,"w")
    f.write(content)
    f.close()

stdpath = r"C:\Users\Michael Obernhumer\Documents\Repository\bericht_converter"
start = stdpath+"\l1dir1"
dataPath = stdpath+"\data.json"
logPath = stdpath+"\log.txt"
stylePath=stdpath+"\style.txt"
filePath="C:\\Users\\Michael Obernhumer\\Documents\\Repository\\bericht_converter\\l1dir1\\l2dir1\\l2dir1file1.md"
convert(filePath,stylePath)