#Example 06: POS Tagging using NLTK


import nltk

from nltk import word_tokenize

sentence = """At eight o'clock on Thursday morning
Arthur didn't feel very good."""

tokens = nltk.word_tokenize(sentence)

print(tokens)

tagged = nltk.pos_tag(tokens)

print(tagged)

# to get help about pos tags
nltk.help.upenn_tagset('IN')

nltk.help.upenn_tagset('NNP')

nltk.help.upenn_tagset('RB')

