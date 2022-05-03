# Authors: Ethan Brooks and Eddie Chen
# Date: 5/2/2022

import spacy
nlp = spacy.load("en_core_web_sm")

class WordBank:
    """Class that creates a valid word bank"""
    valid_words = []

    def __init__(self):
        self.scanText('words.txt')

    def scanText(self, textfile):
        '''opens given file and add valid words to valid words.''' 
        with open(textfile) as words:
            all_words = words.read().lower().split()
            for word in all_words:
                notIn = word not in self.valid_words
                has_vowels = self.contains_vowels(word)
                if len(word) == 4 and word.isalpha() and notIn and has_vowels:
                    self.valid_words.append(word)

    def contains(self, word):
        return word in self.valid_words

    def contains_vowels(self, word):
        ''' check if word has vowels. returns true if it does.'''
        vowels = ['a', 'i', 'o', 'u', 'e', 'y']
        count = 0
        for letter in word:
            if letter in vowels:
                count+=1
        if count > 0:
            return True
        return False

    def getWords(self):
        print(len(self.valid_words))
        return self.valid_words
    

        





        

    
                    

                



