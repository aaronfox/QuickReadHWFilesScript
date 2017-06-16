#! python3
#
# javaToTextRegex.py - converts several Java files to one text file using regex to
# parse where the files should go in order
#
# I personally use the format Problem 1 - 01 in every file to label
# each problem, so I used a regex to parse where that label is in
# each file and then used a list of lists to sort the files in their
# respective order for the text file
#
# NOTE: You must surround the directory and file names with quotes if
# there are space around their respective path names if you are
# running this from the command line

import os, sys, re

# Ensure proper usage
if len(sys.argv) != 3:
    print("Usage: python javaToTextRegex.py java_directory_to_copy_from text_file_to_write_to")
    sys.exit()

# Get the directory name from the first argument
directoryName = sys.argv[1];

# Get the text file name to write to (should end in .txt)
textFile = sys.argv[2]
writeTextFile = open(textFile, "w")

# Create list to store the Java file name and its respective problem orders
# e.g. "javaFileName.java 2 03"
orderedJavaFiles = []

# Create regex to decipher where each java file should be
javaFileRegex = re.compile(r'Problem (\d)(?: -? (\d\d))?')

if os.path.isdir(directoryName):
    fileNames = os.listdir(directoryName)
    for i in range (len(fileNames)):
        if fileNames[i].endswith(".java"):
            readFile = open(directoryName + "\\" + fileNames[i], "r")

            # Create match object returning the Problem number
            mo = javaFileRegex.search(readFile.read())

            if mo is not None:
                # Get number of groups in regex
                numGroups = len(mo.groups())

                # Make new list to store in orderedJavaFiles list
                javaFileWithNumbers = [fileNames[i]]

                if numGroups == 1:
                    javaFileWithNumbers.append(mo.group(1))
                    javaFileWithNumbers.append('00')
                elif numGroups == 2:
                    javaFileWithNumbers.append(mo.group(1))
                    javaFileWithNumbers.append(mo.group(2))
                else:
                    print("I can't parse your file problem numbers.")
                    print("Try changing up the regex up above to fit how your files are labeled.")
            else:
                print("The file " + directoryName + "\\" + fileNames[i] + " could not find the matching regex. Moving on...")
            orderedJavaFiles.append(javaFileWithNumbers)
            print("Getting the text ready to order from " + fileNames[i] + "...")

    # Sort the Java files first by problem number then by subnumber
    orderedJavaFiles = sorted(orderedJavaFiles, key=lambda x: (x[1], x[2]))

    # Write the files in order now
    for file in orderedJavaFiles:
        # file[0] b/c the name is stored at the first element of each list in orderedJavaFiles
        readFile = open(directoryName + "\\" + file[0], "r")
        writeTextFile.write(readFile.read() + "\n\n\n")

    print("Success! Your new text file can be found at " + textFile)
else:
    print("Directory not found. :(")




