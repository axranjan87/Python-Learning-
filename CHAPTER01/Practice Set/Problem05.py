#  Label the program written in problem 4 with comment

# Program Name : Directory Content Viewer
# Objective    : To print contents of a directory using OS module
# Module Used  : os

import os

# Step 1: Define directory path
path = "."

# Step 2: Get list of directory items
items = os.listdir(path)

# Step 3: Display items
for item in items:
    print(item)

    