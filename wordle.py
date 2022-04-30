import tkinter as tk
from tkinter import X, Y, Button, Canvas, StringVar, ttk
import random
from functools import partial
from string import ascii_letters

from setuptools import Command

from words import Words

class Wordle: 
    words = Words()
    valid_words = None
    correctWord = ""
    
    # Word Bank Improvement Needed
    # Fix Button Position
    # Print out correct word
    # Buttons need to disappear after one click

    def __init__(self):
        self.mainWin = tk.Tk()
        self.mainWin.title("Wordle")
        self.mainWin.geometry("400x800")
        self.listEntry = []

        for row in range(6):
            for column in range(4):
                self.var = StringVar()
                self.var.trace(mode="w", callback=self.compareWord)
                e1 = tk.Entry(self.mainWin, font = "Times 70", justify = tk.CENTER, relief = tk.GROOVE, width = 2, textvariable=self.var)
                e1.grid(row = row, column = column)
                self.listEntry.append(e1)

        self.addButtons()
        self.choose_word()
        

    def choose_word(self):
        w = Words()
        self.valid_words = w.getWords()
        length = len(self.valid_words)
        rand_num = random.randint(0, length-1)
        self.correctWord = self.valid_words[rand_num]
        
    def addButtons(self):
        self.btn1 = Button(self.mainWin, text='Enter', command=partial(self.buttonCallBacks, 0)).place(x=325, y=40)
        self.btn2 = Button(self.mainWin, text='Enter', command=partial(self.buttonCallBacks, 1)).place(x=325, y=150)
        self.btn3 = Button(self.mainWin, text='Enter', command=partial(self.buttonCallBacks, 2)).place(x=325, y=260)
        self.btn4 = Button(self.mainWin, text='Enter', command=partial(self.buttonCallBacks, 3)).place(x=325, y=370)
        self.btn5 = Button(self.mainWin, text='Enter', command=partial(self.buttonCallBacks, 4)).place(x=325, y=480)
        self.btn6 = Button(self.mainWin, text='Enter', command=partial(self.buttonCallBacks, 5)).place(x=325, y=590)

    def buttonCallBacks(self, rowNumber):
        print("please work")
        word = self.getRow(rowNumber)
        if self.words.contains(word) == False:
            print("not a word")
        else:
            self.destroy()
        self.checkWin(self.compareWord(word, rowNumber), rowNumber)
        self.disableRow(rowNumber)


    def getRow(self, i):
        i = i * 4
        word = ""
        listEntry2 = []
        for i in self.listEntry[i : i + 4]:
            listEntry2 += [i.get()]
        for i in listEntry2:
            word += i
        return word

    def getRowEntryBoxes(self, i):
        i = i * 4
        return self.listEntry[i : i + 4]
        

    def compareWord(self, guess, rowNumber):
        listCorrectWord = list(self.correctWord)
        listGuess = list(guess)
        colors = []
        rowNumber *= 4
        for i in range(4):
            self.listEntry[rowNumber + i].config({"disabledforeground": "black"})
            if listCorrectWord[i] == listGuess[i]:
                colors.append(2)
                # self.listEntry[rowNumber + i].config({"background": "green"})
                self.listEntry[rowNumber + i].config({"disabledbackground": "green"})
            elif listGuess[i] in listCorrectWord:
                colors.append(1)
                # self.listEntry[rowNumber + i].config({"background":"yellow"})
                self.listEntry[rowNumber + i].config({"disabledbackground":"yellow"})
            else:
                colors.append(0)
                # self.listEntry[rowNumber + i].config({"background":"grey"})
                self.listEntry[rowNumber + i].config({"disabledbackground":"grey"})
        return colors
    
    def checkWin(self, colorList, rowNumber):
        setColorList = set(colorList)
        if setColorList == {2}:
            print("You win!")
            self.mainWin.destroy()
        if rowNumber == 5 and setColorList != {2}:
            print("You Lose!")
            self.mainWin.destroy()

    def disableRow(self, rowNumber):
        listEntryObjects = self.getRowEntryBoxes(rowNumber)
        for i in listEntryObjects:
            i.config(state = "disabled")

    def run(self):
        self.mainWin.mainloop()
        self.choose_word()


w = Wordle()
w.run()
