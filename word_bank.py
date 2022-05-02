# Authors: Ethan Brooks and Eddie Chen
# Date: 5/2/2022

class WordBank:
    """class that a few four letter words"""

    valid_words = []

    def __init__(self):
        self.scanText('words.txt')

    
    def scanText(self, textfile):
        with open(textfile) as words:
            all_words = words.read().lower().split()
            for word in all_words:
                notIn = word not in self.valid_words
                if len(word) == 4 and word.isalpha() and notIn:
                    self.valid_words.append(word)

    # Make a set of words
    def contains(self, word):
        return word in self.valid_words

    def getWords(self):
        print(len(self.valid_words))
        return self.valid_words
    


        





        

    
                    

                



