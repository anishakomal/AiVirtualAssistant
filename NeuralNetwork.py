import numpy as np  # pip install numpy
import nltk
from nltk.stem.porter import PorterStemmer

Stemmer = PorterStemmer()

def tokenize(sentence):  # sentence = jo bhi hum bolenge wo sentence mei aayega as a input
    return nltk.word_tokenize(sentence)


def stem(word):
    return Stemmer.stem(word.lower())


def bag_of_words(tokenized_sentence, words):
    sentence_word = [stem(word) for word in tokenized_sentence]
    bag = np.zeros(len(words), dtype=np.float32)

    for idx, w in enumerate(words):
        if w in sentence_word:
            bag[idx] = 1

    return bag
