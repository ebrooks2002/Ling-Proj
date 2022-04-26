import tkinter as tk
import random

from block_manager import BlockManager
from words import Words

class Wordle: 

    valid_words = None
    correctWord = ""

    def __init__(self):
        self.mainWin = tk.Tk()
        canvas = tk.Canvas(self.mainWin, width = 500, height = 800)
        self.mainWin.title("Wordle")
        self.mainWin.geometry("500x800")
        self.blockManager = BlockManager(canvas)

    def choose_word(self):
        w = Words()
        self.valid_words = w.getWords()
        length = len(self.valid_words)
        print(length)
        rand_num = random.randint(0, length-1)
        self.correctWord = self.valid_words[rand_num]
        print(self.correctWord)
    
    def run(self):
        self.mainWin.mainloop()
        self.choose_word()
        

w = Wordle()
w.run()
