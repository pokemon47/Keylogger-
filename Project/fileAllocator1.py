import shutil
import os
import re
import sys


def safeDirContructor(pathArray):
    pathCon = ""
    for i in range(0,len(pathArray)):
        pathCon += pathArray[i]
        if not (os.path.exists(pathCon) and os.path.isdir(pathCon)):
            os.mkdir(pathCon)

def isEmptyFile(filePath):
    with open(filePath, 'r') as file:
        for line in file:
            if (re.search(r'\S', line)):
                return False
    return True
        
def main():
    srcDir = sys.argv[1] + "\\"
    files = os.listdir(srcDir)
    root = ["Log\\"]
    safeDirContructor(root)

    for filename in files:
        if isEmptyFile(srcDir + filename):
            continue
        dirNames = root + ["".join(s + '\\') for s in filename.split()[0].split("-")]
        safeDirContructor(dirNames)
        newFilename = '-'.join(reversed((''.join(filename.split()[2:])).split('-'))) + "_.txt"
        shutil.copy(srcDir + filename, ''.join(dirNames) + newFilename)

main()