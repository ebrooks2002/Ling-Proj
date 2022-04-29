import tkinter as tk
from tkinter import X, Y, Button, Canvas, StringVar, ttk
import random
from functools import partial
from string import ascii_letters

from setuptools import Command

from words import Words

class Wordle: 
    w = Words()
    valid_words = None
    correctWord = ""
    
    def __init__(self):
        self.mainWin = tk.Tk()
        self.mainWin.title("Wordle")
        self.mainWin.geometry("400x800")
        #self.canvas = Canvas(self.mainWin)
        self.listEntry = []
        # Use state = DISABLED after a row has been completed
        for row in range(6):
            for column in range(4):
                self.var = StringVar()
                self.var.trace(mode="w", callback=self.compareWord)
                e1 = tk.Entry(self.mainWin, font = "Times 70", justify = tk.CENTER, relief = tk.GROOVE, width = 2, textvariable=self.var)
                e1.grid(row = row, column = column)
                e1.bind("ascii_letters", partial(self.testEntryResponse, e1))
                self.listEntry.append(e1)

        self.addButtons()
        self.choose_word()
        

    def choose_word(self):
        w = Words()
        self.valid_words = w.getWords()
        length = len(self.valid_words)
        rand_num = random.randint(0, length-1)
        self.correctWord = self.valid_words[rand_num]
        

    def testEntryResponse(self, entry, event):
        if event.keysym == "Return":
            print("Return pressed")
            
            # txt = entryBox.get()
            # print(txt)

    def addButtons(self):
        self.btn1 = Button(self.mainWin, text='Enter', command=partial(self.buttonCallBacks, 0)).place(x=330, y=40)
        self.btn2 = Button(self.mainWin, text='Enter', command=partial(self.buttonCallBacks, 1)).place(x=330, y=130)
        self.btn3 = Button(self.mainWin, text='Enter', command=partial(self.buttonCallBacks, 2)).place(x=330, y=220)
        self.btn4 = Button(self.mainWin, text='Enter', command=partial(self.buttonCallBacks, 3)).place(x=330, y=310)
        self.btn5 = Button(self.mainWin, text='Enter', command=partial(self.buttonCallBacks, 4)).place(x=330, y=400)
        self.btn6 = Button(self.mainWin, text='Enter', command=partial(self.buttonCallBacks, 5)).place(x=330, y=490)

    def buttonCallBacks(self, rowNumber):
        print("please work")
        word = self.getRow(rowNumber)
        if self.w.contains(word) == False:
            print("not a word")
        self.compareWord(word, rowNumber)

    def getRow(self, i):
        i = i * 4
        word = ""
        listEntry2 = []
        for i in self.listEntry[i : i + 4]:
            listEntry2 += [i.get()]
        for i in listEntry2:
            word += i
        return word

    def compareWord(self, guess, rowNumber):
        listCorrectWord = list(self.correctWord)
        listGuess = list(guess)
        colors = []
        rowNumber *= 4
        for i in range(4):
            if listCorrectWord[i] == listGuess[i]:
                colors.append(2)
                self.listEntry[rowNumber + i].config({"background": "green"})
                
            elif listGuess[i] in listCorrectWord:
                colors.append(1)
                self.listEntry[rowNumber + i].config({"background":"yellow"})
                
            else:
                colors.append(0)
                self.listEntry[rowNumber + i].config({"background":"grey"})
                
        print(colors)

    def run(self):
        self.mainWin.mainloop()
        self.choose_word()


w = Wordle()
w.run()
