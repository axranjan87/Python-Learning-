# WAPP to print contents of a directory using the OS modules search online for the function which does that

import os

# path of directory
path = "."

# list directory contents
files = os.listdir(path)

print("Contents of the directory are:")
for file in files:
    print(file)



'''Explation

import os → imports the OS module.

os.listdir(path) → returns a list of all files and folders in that directory.

"." means current directory.

The for loop prints each file name.'''

