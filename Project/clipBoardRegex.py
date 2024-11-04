import re
import sys

# needs one command line arguement to work, it should be the path/filename of the Logclip file


def searchFile():
    specialIdentifier = "e236829f840cb1e1bb04a7305d33a95ff342cbe4954166ff23ab2037d2b52216\n"
    # the special identifier above is the same one used in the keySender4.py file
    passwordPattern = r'[ ]{0,1}(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!#%*?&])[A-Za-z\d@$!%#*?&]{8,}[ \n]{0,1}'

    srcFile = open(sys.argv[1], 'r')
    isNewLoc = False
    curLoc = ""
    lineCounter = 1
    for line in srcFile:
        if isNewLoc:            
            curLoc = line.strip()
            isNewLoc = False
        elif line == specialIdentifier:
            isNewLoc = True
        else:
            finds = re.findall(passwordPattern, line)
            for find in finds:
                print(f"{find.strip()} | LINE {lineCounter} | {curLoc}")
        lineCounter += 1        
searchFile()