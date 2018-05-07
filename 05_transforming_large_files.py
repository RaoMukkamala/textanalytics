# Example 5a: copy first 50000 lines from a very large file 
# Note that here we read the data line by line, but not whole file at once
# like in example 1. This strategy is efficient and helps a lot in reading 
# and writing the large files. 

import os

currentDir = os.getcwd()

sourceFile = os.path.join(currentDir, 'data', 'Hillary_50000_lines.csv')


destinationPath = os.path.join(currentDir, 'data', 'Hillary_25000_lines.csv')

with open(destinationPath, 'w', encoding='utf-8') as fw:
   with open(sourceFile, 'r', encoding='utf-8') as fr:
      for i in range(25000):
         fw.write(fr.readline())




#Example 5b: 
# Here the file Hillary_50000_lines.csv is comma seperated, so we transform it into semicolon seperated. 

import os
import csv

currentDir = os.getcwd()

sourceFile = os.path.join(currentDir, 'data', 'Hillary_50000_lines.csv')


destinationPath = os.path.join(currentDir, 'data', 'Hillary_50000_lines_transformed.csv')



with open(sourceFile) as csvfile:
   fbDataReader = csv.reader(csvfile, delimiter=',',)
   with open(destinationPath, 'w', newline='') as writeFile:
      fbTextWriter = csv.writer(writeFile, delimiter=';',quoting=csv.QUOTE_MINIMAL)
      for row in fbDataReader:
         print(str(len(row)))
         if len(row) != 20: 
            continue
         row[19] = row[19].replace(';',' ')
         fbTextWriter.writerow(row)

   writeFile.close()

print('done!')

