import tkinter as tk

class Wordle:
    def __init__(self):
        self.mainWin = tk.Tk()
        self.mainWin.title("Wordle")
        self.mainWin.geometry("500x800")

    def run(self):
        self.mainWin.mainloop()


w = Wordle()
w.run()