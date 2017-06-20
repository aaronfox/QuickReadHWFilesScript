#! python3
#
# javaToText.py - converts several Java files to one text file
#
# NOTE: You must surround the directory and file names with quotes if
# there are space around their respective path names if you are
# running this from the command line
#
# I strongly recommend you use the javaToTextRegex.py instead of this
# as it will order your files accordingly instead of alphabetically like
# this. Unless, of course, that is what you want

import os, sys

# Ensure proper usage
if len(sys.argv) != 3:
    print("Usage: python javaToText.py java_directory_to_copy_from text_file_to_write_to")
    sys.exit()

# Get the directory name from the first argument
directoryName = sys.argv[1];

# Get the text file name to write to (should end in .txt)
textFile = sys.argv[2]
writeTextFile = open(textFile, "w")

if os.path.isdir(directoryName):
    fileNames = os.listdir(directoryName)
    for i in range (len(fileNames)):
        readFile = open(directoryName + "\\" + fileNames[i], "r")
        writeTextFile.write(readFile.read() + "\n\n\n")
        print("Writing the text from " + fileNames[i] + "...")
    print("Success!")
else:
    print("Directory not found. :(")



