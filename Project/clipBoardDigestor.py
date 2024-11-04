import os
import re
import sys

# needs one command line arguement to work, it should be the path/filename of the Logclip file
# HALTED FOR WORK

def safeDirContructor(pathArray):
    pathCon = ""
    for i in range(0,len(pathArray)):
        pathCon += pathArray[i]
        if not (os.path.exists(pathCon) and os.path.isdir(pathCon)):
            os.mkdir(pathCon)

        
def fileMaker(filename, content):
    srcDir = sys.argv[1] + "\\"
    files = os.listdir(srcDir)
    root = ["ClipLog\\"]
    safeDirContructor(root)

    srcFile = open(sys.argv[1], 'r')
