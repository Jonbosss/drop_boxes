import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title('Drop Boxes')
root.geometry('400x400')

clicked = StringVar()

drop = OptionMenu(root, clicked, "Monday", "Tuesday",
                  "Wednesday", "Thursday", "Friday")
drop.pack()


root.mainloop()
