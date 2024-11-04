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

# def isEmptyFile(filePath):
#     with open(filePath, 'r') as file:
#         for line in file:
#             if (re.search(r'\S', line)):
#                 return False
#     return True
        
def fileMaker(filename, content):
    srcDir = sys.argv[1] + "\\"
    files = os.listdir(srcDir)
    root = ["ClipLog\\"]
    safeDirContructor(root)

    srcFile = open(sys.argv[1], 'r')



    # for filename in files:
    #     dirNames = root + ["".join(s + '\\') for s in filename.split()[0].split("-")]
    #     safeDirContructor(dirNames)
    #     newFilename = '-'.join(reversed((''.join(filename.split()[2:])).split('-'))) + "_.txt"