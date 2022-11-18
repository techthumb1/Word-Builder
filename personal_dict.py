# Install libraries: pip install -r requirements.txt
# Run: python personal_dict.py
# pip install PyDictionary
# pip install Random-Word

import os
import sys
import pprint
from PyDictionary import PyDictionary
from random_word import RandomWords


class PersonalDict:

    """
    Randomly generate a word and print it's meaning, synonyms, antonyms
    """

    def __init__(self):
        self.dictionary = PyDictionary()
        self.rw = RandomWords()
        self.words = []
        self.word = None
        self.word_meaning = None
        self.word_synonyms = None
        self.word_antonyms = None
        #self.word_examples = None
        #self.word_pronunciation = None

    def get_random_word(self):
        self.word = self.rw.get_random_word()
        return self.word

    def get_word_meaning(self):
        self.word_meaning = self.dictionary.meaning(self.word)
        return self.word_meaning

    def get_word_synonyms(self):
        self.word_synonyms = self.dictionary.synonym(self.word)
        return self.word_synonyms

    def get_word_antonyms(self):
        self.word_antonyms = self.dictionary.antonym(self.word)
        return self.word_antonyms

    #def get_word_examples(self):
    #    self.word_examples = self.dictionary.examples(self.word)
    #    return self.word_examples

    #def get_word_pronunciation(self):
    #    self.word_pronunciation = self.dictionary.pronunciation(self.word)
    #    return self.word_pronunciation

    def get_word(self):
        self.word = self.get_random_word()
        self.word_meaning = self.get_word_meaning()
        self.word_synonyms = self.get_word_synonyms()
        self.word_antonyms = self.get_word_antonyms()
        #self.word_examples = self.get_word_examples()
        #self.word_pronunciation = self.get_word_pronunciation()
        return self.word, self.word_meaning, self.word_synonyms, self.word_antonyms#, self.word_examples, self.word_pronunciation

    def get_words(self, num_words):
        for i in range(num_words):
            self.get_word()
            self.words.append(self.word)
        return self.words

    def print_word(self):
        print(self.word)
        print(self.word_meaning)
        print(self.word_synonyms)
        print(self.word_antonyms)
        #print(self.word_examples)
        #print(self.word_pronunciation)

    def print_words(self):
        for word in self.words:
            print(word)

    #def save_word(self):
    #    with open('words.txt', 'a') as f:
    #        f.write(self.word + '\n')


if __name__ == '__main__':
    pd = PersonalDict()
    pd.get_words(10)
    pd.print_words()
    #pd.save_word()


# Path: personal_dict.py
# Install libraries: pip install -r requirements.txt
# Run: python personal_dict.py
