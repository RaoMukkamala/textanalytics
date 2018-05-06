# Example 4: Writing to a file and save it to disk

import os

currentDir = os.getcwd()

targetFilePath = os.path.join(currentDir, 'data', 'temp.txt')


with open(targetFilePath, 'w') as f:
   f.write("hello world \n")
   f.write("some more text with no line ending")
   f.write("more and more text ")


# read a file line by line
with open(targetFilePath) as f:
    lines = f.readlines()

lines
