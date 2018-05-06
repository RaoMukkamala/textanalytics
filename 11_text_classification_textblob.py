# Example 10: Text classification using text blob



from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob

train = [
    ('I love this sandwich.', 'pos'),
    ('This is an amazing place!', 'pos'),
    ('I feel very good about these beers.', 'pos'),
    ('This is my best work.', 'pos'),
    ("What an awesome view", 'pos'),
    ('I do not like this restaurant', 'neg'),
    ('I am tired of this stuff.', 'neg'),
    ("I can't deal with this", 'neg'),
    ('He is my sworn enemy!', 'neg'),
    ('My boss is horrible.', 'neg')
]
cls = NaiveBayesClassifier(train)

# Testing accuracy with a testset
test = [
    ('The beer was good.', 'pos'),
    ('I do not enjoy my job', 'neg'),
    ("I ain't feeling dandy today.", 'neg'),
    ("I feel amazing!", 'pos'),
    ('Gary is a friend of mine.', 'pos'),
    ("I can't believe I'm doing this.", 'neg')
]

print(cls.accuracy(test))

print(cls.classify("Their burgers are amazing"))
print(cls.classify("I don't like their pizza."))

from textblob import TextBlob

blob = TextBlob("The beer was amazing. "
                "But the hangover was horrible. My boss was not happy.",
                classifier=cls)
print(blob.classify())


# Fetching label probablities
prob_dist = cls.prob_classify("Their burgers are amazing")

print(prob_dist.max())

print(round(prob_dist.prob("pos"), 2))

print(round(prob_dist.prob("neg"), 2))