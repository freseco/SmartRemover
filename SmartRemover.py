"""
    Author: Francisco Reseco
    Date: 01/05/2018
    Description: Script to remove the repetitive text in a list of files in a current directorio.
"""
import os
import string
import sys
from os import listdir
from os.path import isfile, join

#Ask to the user the string to remove
condition=""
ListText=[]
while True:
    condition=input("Enter text to remove(twice Press Enter to start the process):")
    if condition=="":
        break
    ListText.append(condition)

#print(ListText)
mypath=os.getcwd()

#file list in the directory
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]


#rename all files removing the text in the Listtext, skiping the python file
for filename in onlyfiles:
    
    if __file__ == filename:
        continue
    #save the original file name
    newname=filename
    
    #remove the strings in the file name
    for textremove in ListText:
        newname = newname.replace(textremove,"")
        
    #rename the file
    if newname!=filename:
        try:
            os.rename(filename,newname)
        except PermissionError:
            print("Error to rename the file: ", filename)
        
#Exit of the program
#input("Press enter to exit")
