import os
import sys
import legend
import fileinput
import re
dirList = os.listdir()
dirList.remove('decoding.py')
dirList.remove('legend.py')
dirList.remove('__pycache__')

print('Select a file to decode, 0-x choices (0 being the first one)')
print(dirList)
userChoice=int(input("Type a number:"))
workingFile = dirList[userChoice]

dec = open('decoded.txt', 'w')
with open(workingFile, 'r+') as f:
    linef = f.readlines()
    for line in linef:
        if len(line)<1: continue
        else:
            xcon=68
            lineList = re.split('=|,|\n', line) #pulls out numbers only
            firstword = lineList[0]
            twodig = [x for x in lineList if len(x)<3] #takes out the big number
            newtext = twodig
            while xcon > 0:
                xstr = str(xcon)
                newCode = legend.dlist[xcon-1]
                
                newtext = [re.sub(xstr, newCode, i) for i in newtext] #decodes the list element by element
                xcon -= 1
            xcon=68 #resets the counter
            dec.write(firstword+' = ') #formatting and writing down the results
            for x in range(len(newtext)):
                dec.write(newtext[x])
                dec.write(' ')
            dec.write("\n")