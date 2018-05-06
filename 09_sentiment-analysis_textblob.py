# Example 08: Sentiment Analysis with textblob 

from textblob import TextBlob

tblob =TextBlob("Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex.")
tblob.words
tblob.sentences

tblob2 = TextBlob("I hate you")
tblob2.sentiment

tblob2 = TextBlob("The world hates you")
tblob2.sentiment

tblob2 = TextBlob("What a wonderful day!!")
tblob2.sentiment

tblob2 = TextBlob("Sun is shining!!")
tblob2.sentiment

tblob2 = TextBlob("Sun is shining very bright")
tblob2.sentiment


