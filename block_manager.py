import tkinter as tk

class BlockManager:
    def __init__(self, canvas):

        canvas.grid(row=10, column=0)
        canvas.create_rectangle(10, 10, 100, 100, fill = "green")
        canvas.grid(row=20, column=0)
        canvas.create_rectangle(110, 110, 200, 200, fill = "green")
    