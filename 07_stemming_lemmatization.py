# Example 07: Stemming and lemmatization

import nltk
from nltk.stem.porter import PorterStemmer
st = PorterStemmer()
# lemmatization
wnl = nltk.WordNetLemmatizer()

st.stem("ponies")
wnl.lemmatize("ponies")

st.stem("example")
wnl.lemmatize("example")

st.stem("equivalent")
wnl.lemmatize("equivalent")


# Example 6: on tokenization, stemming and lemmatization
from nltk import word_tokenize
from nltk.stem.porter import PorterStemmer

raw = """DENNIS: Listen, strange women lying in ponds distributing swords is no basis for a system of government.  Supreme executive power derives from a mandate from the masses, not from some farcical aquatic ceremony."""
tokens = word_tokenize(raw)
porter = nltk.PorterStemmer()
lancaster = nltk.LancasterStemmer()
wnl = nltk.WordNetLemmatizer()

print('printing tokens using PorterStemmer \n')
print([porter.stem(t) for t in tokens])
print('\n')
print('printing tokens using LancasterStemmer \n')
print([lancaster.stem(t) for t in tokens])
print('\n')
print('printing tokens using WordNetLemmatizer \n')
print([wnl.lemmatize(t) for t in tokens])

