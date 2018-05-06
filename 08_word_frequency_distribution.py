# Example 11: Cumulative Frequency distributions

import os
import re

import nltk
from nltk.book import *
from nltk.corpus import stopwords
stop_words = stopwords.words('english')

removeWordList = [' ', 'I']


currentDir = os.getcwd()

textFilePath = os.path.join(currentDir, 'data', 'austen-emma.txt')


with open(textFilePath) as filereader:
   text = filereader.read()

tokens = nltk.word_tokenize(text)

raw_words=re.split(r'\W+|\d+', text)

[word.lower() for word in raw_words]

good_words = [word for word in raw_words if (word not in stop_words) and (word not in removeWordList)]

fdist1 = nltk.FreqDist(good_words)


# prints first 50 words with frequency 
print(fdist1.most_common(50))


vocabulary1 = list(fdist1)

print(vocabulary1[:50])

# print top 100 words that occur frequently.
for (word, fre) in fdist1.most_common(50):
   print(word + ": " + str(fdist1[word]))

for word in vocabulary1[:100]:
   print(word + ": " + str(fdist1[word]))

fdist1['government']

fdist1.plot(50, cumulative=True)

fdist1.plot(50, cumulative=False)