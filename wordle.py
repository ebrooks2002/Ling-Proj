# Authors: Ethan Brooks and Eddie Chen
# Date: 5/2/2022

import string
import tkinter as tk
from tkinter import CENTER, Button, Label, StringVar
import random
from functools import partial
from word_bank import WordBank

class Wordle: 
    """class that runs main wordle game"""
    words = WordBank()
    valid_words = None
    mainWin = tk.Tk()
    correctWord = ""
    unused_letters = list(string.ascii_lowercase)
    used_letters = set([])
    used = Label(mainWin)
    unused = Label(mainWin)
    
    def __init__(self):
        '''Constructor initalizes main window, buttons, entryboxes. chooses correct word.'''
        self.mainWin.title("Wordle")
        self.mainWin.geometry("550x800")
        self.listEntry = [] 
        self.addEntryBoxes()
        self.addButtons()
        self.choose_word()

    def addEntryBoxes(self):
        '''Add entry boxes to input letters to mainWin using nested for loop'''
        for row in range(6):
            for column in range(4):
                self.var = StringVar()
                self.var.trace(mode="w", callback=self.compareWord)
                e1 = tk.Entry(self.mainWin, font = "Times 70", justify = tk.CENTER, relief = tk.GROOVE, width = 2, textvariable=self.var)
                e1.grid(row = row, column = column)
                self.listEntry.append(e1)
        
    def choose_word(self):
        ''' chooses a random word from the word bank'''
        w = WordBank()
        self.valid_words = w.getWords()
        length = len(self.valid_words)
        rand_num = random.randint(0, length-1)
        self.correctWord = self.valid_words[rand_num]
        
    def addButtons(self):
        '''Buttons added to mainWin for submitting a word guess'''
        self.btn1 = Button(self.mainWin, text = 'Enter', command = partial(self.buttonCallBacks, 0)).place(x = 400, y = 40)
        self.btn2 = Button(self.mainWin, text = 'Enter', command = partial(self.buttonCallBacks, 1)).place(x = 400, y = 150)
        self.btn3 = Button(self.mainWin, text = 'Enter', command = partial(self.buttonCallBacks, 2)).place(x = 400, y = 260)
        self.btn4 = Button(self.mainWin, text = 'Enter', command = partial(self.buttonCallBacks, 3)).place(x = 400, y = 370)
        self.btn5 = Button(self.mainWin, text = 'Enter', command = partial(self.buttonCallBacks, 4)).place(x = 400, y = 480)
        self.btn6 = Button(self.mainWin, text = 'Enter', command = partial(self.buttonCallBacks, 5)).place(x = 400, y = 590)
        
    def buttonCallBacks(self, rowNumber):
        '''Everytime a button is pressed, get the letters in the entry boxes, 
            check if it is in word bank, and then check letters.'''
        word = self.get_rows_word(rowNumber)
        if self.words.contains(word) == False:
            return None
        self.manageUsedLetters(word)
        self.checkWin(self.compareWord(word, rowNumber), rowNumber)
        self.disableRow(rowNumber)

    def manageUsedLetters(self, word):
        '''If letter has been used, add to used letters and remove from unused letters.
            Also updates the label on the screen.'''
        Wordle.unused.destroy()
        for letter in word:
            letter = letter.lower()
            if letter in self.unused_letters:
                self.used_letters.add(letter)
                self.unused_letters.remove(letter)
        Wordle.used = Label(self.mainWin, text="used: "+ str(self.used_letters),font=("arial", 14))
        Wordle.used.place(x=10, y=650)
        Wordle.unused = Label(self.mainWin, text="unused: "+str(self.unused_letters),font=("arial", 14))
        Wordle.unused.place(x=10, y=700)
        
    def get_rows_word(self, i):
        '''Returns the word for the row that was given. 0 for i returns first
           word entered.'''
        i = i * 4
        word = ""
        listEntry2 = []
        for i in self.listEntry[i : i + 4]:
            listEntry2 += [i.get()]
        for i in listEntry2:
            word += i
        return word.lower()

    def get_rows_entrys(self, i):
        '''Returns entry boxes for the row given. 0 for i returns first row of boxes'''
        i = i * 4
        return self.listEntry[i : i + 4]
        
    def compareWord(self, guess, rowNumber):
        '''Compares the guess with the correct word and colors the entry
           boxes accordingly.'''
        listCorrectWord = list(self.correctWord)
        listGuess = list(guess)
        colors = []
        rowNumber *= 4
        for i in range(4):
            self.listEntry[rowNumber + i].config({"disabledforeground": "black"})
            if listCorrectWord[i] == listGuess[i]:
                colors.append(2)
                self.listEntry[rowNumber + i].config({"disabledbackground": "green"})
            elif listGuess[i] in listCorrectWord:
                colors.append(1)
                self.listEntry[rowNumber + i].config({"disabledbackground":"yellow"})
            else:
                colors.append(0)
                self.listEntry[rowNumber + i].config({"disabledbackground":"grey"})

        return colors
    
    def checkWin(self, colorList, rowNumber):
        '''If the color list is only contains 2's, the player has won. Creates labels to display
           win/lose.'''
        setColorList = set(colorList)
        if setColorList == {2}:
            print("you won")
            Label(self.mainWin, anchor=CENTER, text="You Win!", font=("Arial",40), bg="green").place(x=100, y=300)
        if rowNumber == 5 and setColorList != {2}:       
            Label(self.mainWin, anchor=CENTER, text=f"You Lose! Correct Word: {self.correctWord}", font=("Arial",30), bg="red").place(x=80, y=300)
            print("you lost")

    def disableRow(self, rowNumber):
        '''disables entry boxes so users can only make one guess per row.'''
        listEntryObjects = self.get_rows_entrys(rowNumber)
        for i in listEntryObjects:
            i.config(state = "disabled")

    def run(self):
        '''creates main game loop'''
        print(self.correctWord)
        self.mainWin.mainloop()
        
if __name__ == "__main__":
    w = Wordle()
    w.run()
