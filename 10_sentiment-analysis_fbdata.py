import os
import csv
from textblob import TextBlob

currentDir = os.getcwd()

sourceFile = os.path.join(currentDir, 'data', 'Hillary_50000_lines.csv')

destinationPath = os.path.join(currentDir, 'data', 'Hillary_50000_lines_sentiment.csv')

with open(sourceFile) as csvfile:
    fbDataReader = csv.reader(csvfile, delimiter=',', )
    header = next(fbDataReader)
    header = ['Polarity', 'Subjectivity'] + header
    with open(destinationPath, 'w', newline='') as writeFile:
        fbTextWriter = csv.writer(writeFile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        fbTextWriter.writerow(header)
        for row in fbDataReader:
            if len(row) != 20:
                continue
            # if the length of text is less than 50 then skip the row.
            if len(row[19]) < 50:
                continue

            tblob = TextBlob(row[19])
            sentilist = [format(tblob.sentiment.polarity, '.2f'), format(tblob.sentiment.subjectivity, '.2f')]
            fbTextWriter.writerow(sentilist + row)
    writeFile.close()
