import tkinter as tk

class BlockManager:
    def __init__(self, canvas):
        """Prints the rectangles of Wordle onto the screen."""
        canvas.grid(row=10, column=0)
        length = 90
        buffer = 10
        x1 = 10
        x2 = 100
        y1 = 10
        y2 = 100
        
        for x in range(6):
            canvas.create_rectangle(x1, x2, y1, y2, fill = "green")
            x1 += x1 + x2
            x2 += x2 + buffer + length
            y1 += 
            y2 += 
            for y in range(6):
                
                

                # rect1 = canvas.create_rectangle(10, 10, 100, 100, fill = "green")
                # rect2 = canvas.create_rectangle(10, 110, 100, 200, fill = "green")
                # rect3 = canvas.create_rectangle(10, 210, 100, 300, fill = "green")
                # rect4 = canvas.create_rectangle(10, 310, 100, 400, fill = "green")
                # rect5 = canvas.create_rectangle(10, 410, 100, 500, fill = "green")
                # rect6 = canvas.create_rectangle(10, 510, 100, 600, fill = "green")
                # rect7 = canvas.create_rectangle(110, 10, 200, 100, fill = "green")