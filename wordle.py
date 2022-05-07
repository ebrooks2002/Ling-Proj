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


"""
How well do English speakers know 4-lettered uncommonly used words?
Given an unknown obscure 4-letter word and 6 tries, how often were players going to succeed in finding this word?

1. How does the code address your narrow research question? For example, what information or 
secondary data did you derive from primary sources?
Inside the code we were able to eliminate words that weren't four letters, that had numbers, and that didn't have vowels from our list of words that
we got from our primary source. (WHAT IS OUR PRIMARY SOURCE AND WHERE DID WE GET IT FROM?)

2. What is known about the phenomenon you are looking at? Consult and cite at least one source 
(may be informal) that contributes to the research question you have.
Reseach paper:  Word clouds help create a visualization to represent text data (Dickinson, 2010;McNaught & Lam, 2010
Research Paper: Language Learning: Comparing Native and Non-Native Speaker Vocabulary (https://blog.cyracom.com/the-lifelong-pursuit-of-language-learning-how-the-vocabularies-of-native-and-non-native-speakers-compare#:~:text=The%20researchers%20found%20that%20native,from%20ages%2016%20to%2050.)

3. What are your actual findings, if any? Basic descriptive statistics are alright to use here (i.e., 
means, ranges, counts or proportions).
Eddie played 10 games; Ethan played 10 games. Collectively, we played a total of 20 games. Of these 20 games, we won a 
total of 10 games. That means we had a 50% win rate. We would have the same probability of winning a coin flip. We think
that a 50% win rate is relatively low. In addition to this, of the games that we won, the distribution of number of tries is heavily
skewed to the right since we guessed the word in 5 to 6 tries. This is definitely more difficult than Wordle where 96% of games end in wins (https://benn.substack.com/p/how-to-play-wordle?s=r).

4. How does the research contribute to the broad research question you asked? What are its 
limitations in answering the “big picture” question?
We think that the win-rate of our Wordle game helps us answer the amount of 4-lettered uncommonly used words that an average English speaker knows. However,
some limitations may include the hints that our Wordle game gives the user. Even if they do not know the 4-letter word, they still have the 
opportunity to guess that word. This could affect our understanding of the data as the win-rate may not truly reflect their knowledge/recognition of the
4-letter word. However, the win-rate statistic is probably our best metric for understanding how well/how many uncommon 4-letter words that an average
English speaker knows.

5. What is a future direction research like this could take? How can this be expanded or 
complement other work?
One direction that we think that this research could take is to revive the usage of obscure 4-letter words by bringing awarenness to them. An attempt at
expansion of this research question is instead of 4-letter words, we observe 5-letter words, 6-letter words, etc.

"""