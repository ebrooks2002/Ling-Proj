import tkinter as tk
from block_manager import BlockManager

class Wordle:
    def __init__(self):
        self.mainWin = tk.Tk()
        canvas = tk.Canvas(self.mainWin, width = 500, height = 800)

        self.mainWin.title("Wordle")
        self.mainWin.geometry("500x800")
        self.blockManager = BlockManager(canvas)

    def run(self):
        self.mainWin.mainloop()
        

w = Wordle()
w.run()