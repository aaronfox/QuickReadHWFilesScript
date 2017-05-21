# QuickReadHWFilesScript
Posting so my classmates can use ~ our Java professor makes us concatenate all of our assignments into one text file, so this quick and dirty script does that for us.
## Usage <sup><sub>(For Windows, since that's the overwhelming majority of us CECS students)<sub><sup>

1. Download the python script
2. Copy the script's exact path name and insert and create a batch file, like that found in javaToText.bat: 
```
@py.exe "C:\example\full\python\executable\path\javaToText.py" %*
@pause
```
3. Place the batch file into a batch file directory (create one if you don't already have one)
4. Place the directory from number 3 into your PATH system environmental variable
5. Type [Windows Key + R] to bring up `Run`
6. Type your desired command from Run and, well, run it. Make sure to add quotes around your file/ directory paths if there are spaces anywhere in their path. Otherwise this script won't understand how many arguments there really are and how to use them.
e.g. `javaToText "C:\Users\aaron\CECS_220\src\assignment_01" "C:\CECS 220\Assignment_01\Last_First_Source_Code.txt"` 

The usage, taken from javaToText.py, is:
`Usage: python javaToText.py java_directory_to_copy_from text_file_to_write_to`

<em>Note that the destination file name should probably end in `.txt` here<em>
