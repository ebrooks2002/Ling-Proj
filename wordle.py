from curses import BUTTON1_CLICKED
from gc import callbacks
import tkinter as tk
from tkinter import X, Y, Button, Canvas, ttk
import random
from functools import partial
from string import ascii_letters
from turtle import onclick

from block_manager import BlockManager
from words import Words

class Wordle: 

    valid_words = None
    correctWord = ""
    
    def __init__(self):
        self.mainWin = tk.Tk()
        self.mainWin.title("Wordle")
        self.mainWin.geometry("400x800")
        #self.canvas = Canvas(self.mainWin)
        listEntry = []
        # Use state = DISABLED after a row has been completed
        for row in range(6):
            for column in range(4):
                e1 = tk.Entry(self.mainWin, font = "Times 70", justify = tk.CENTER, relief = tk.GROOVE, width = 2)
                e1.grid(row = row, column = column)
                e1.bind("ascii_letters", partial(self.testEntryResponse, e1))
                listEntry.append(e1)

        self.addButtons()

        print(listEntry)

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

    def addButtons(self):
        self.btn1 = Button(self.mainWin, text='Enter', command=self.buttonCallBacks).place(x=330, y=40)
        self.btn2 = Button(self.mainWin, text='Enter').place(x=330, y=130)
        self.btn3 = Button(self.mainWin, text='Enter').place(x=330, y=220)
        self.btn4 = Button(self.mainWin, text='Enter').place(x=330, y=310)
        self.btn5 = Button(self.mainWin, text='Enter').place(x=330, y=400)
        self.btn6 = Button(self.mainWin, text='Enter').place(x=330, y=490)

    def buttonCallBacks(self):
        print("please work")
        
        
    def run(self):
        self.mainWin.mainloop()
        self.choose_word()

        

w = Wordle()
w.run()
