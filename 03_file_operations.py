# Example 3: read file contents at once

import os

currentDir = os.getcwd()

textFilePath = os.path.join(currentDir, 'data', 'shakespeare-macbeth.txt')


textFilePath = textFilePath.replace('\\', '/')

with open(textFilePath) as f:
    text = f.read()

# read a file line by line
with open(textFilePath) as f:
    lines = f.readlines()

# reading the first line
lines[0]

#reading the last line
lines[-1]

# reading first 15 lins
lines[0:15]

# reading last 15 lins
lines[-15:]

