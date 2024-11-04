import re
import sys
import os

# requires a command line arguement, the dirname/path of where the processed files are stored 


def searchFile(filename):
    if not (os.path.isfile(filename)):
        return
    passwordPattern = r'[ ]{0,1}(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!#%*?&])[A-Za-z\d@$!%#*?&]{8,}[ \n]{0,1}'
    with open(filename, 'r') as file:
        lineCounter = 1
        for line in file:
            finds = re.findall(passwordPattern, line)
            # if (finds):
            #     print(finds)
            for find in finds:
                print(f"{find.strip()} | LINE {lineCounter} | PATH {filename}")
            lineCounter += 1

def recFinder(pathname):
    if (os.path.isfile(pathname)):
        searchFile(pathname)
        return
    dirContent = os.listdir(pathname)
    for value in dirContent:
        pathValue = pathname + "\\" + value
        recFinder(pathValue)



recFinder(sys.argv[1])