from tkinter import *

root = Tk()     # Making a Window

# Text Widgets
myLabel = Label(root, text="Hello World!")
myLabel2 = Label(root, text="I am Imran")

# Packing all the widgets
# myLabel.pack()
# myLabel2.pack()

# using Grid System
myLabel.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)

# Make the program to loop continually
root.mainloop()
