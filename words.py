
class Words:

    def __init__(self):
        with open('words.txt') as words:
            words = words.read().split()
            for word in words:
                if len(word) == 4:

w = Words()
