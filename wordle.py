import tkinter as tk
from tkinter import ttk
import random
from functools import partial
from string import ascii_letters

from block_manager import BlockManager
from words import Words

class Wordle: 

    valid_words = None
    correctWord = ""

    def __init__(self):
        self.mainWin = tk.Tk()
        self.mainWin.title("Wordle")
        # canvas = tk.Canvas(self.mainWin, width = 500, height = 800)
        # canvas.grid(row = 0, column = 0)
        listEntry = []
        # Use state = DISABLED after a row has been completed
        for row in range(6):
            for column in range(4):
                e1 = tk.Entry(self.mainWin, font = "Times 70", justify = tk.CENTER, relief = tk.GROOVE, width = 2)
                e1.grid(row = row, column = column)
                e1.bind("ascii_letters", partial(self.testEntryResponse, e1))
                listEntry.append(e1)

        print(listEntry)

        # self.mainWin.geometry("500x800")
        # self.blockManager = BlockManager(self.mainWin)


    def choose_word(self):
        w = Words()
        self.valid_words = w.getWords()
        length = len(self.valid_words)
        print(length)
        rand_num = random.randint(0, length-1)
        self.correctWord = self.valid_words[rand_num]
        print(self.correctWord)

    def testEntryResponse(self, entry, event):
        if event.keysym == "Return":
            print("Return pressed")
            print(entry.get())
            # txt = entryBox.get()
            # print(txt)
            



    def run(self):
        self.mainWin.mainloop()
        self.choose_word()
        

w = Wordle()
w.run()
