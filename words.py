""" class that returns all valid four letter words"""
class Words:

    valid_words = []

    def __init__(self,):
        with open('words.txt') as words:
            all_words = words.read().lower().split()
            for word in all_words:
                if (len(word) == 4) and (word.isalpha()):
                    self.valid_words.append(word)

    def getWords(self):
        return self.valid_words
                    



