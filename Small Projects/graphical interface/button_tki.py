from tkinter import *

root = Tk()

# Defying the function after clicking the button
def clickme():
    myLabel = Label(root, text="I clicked the Button!!")
    myLabel.pack()


# Creating Button Widgets
myButton = Button(root, text="Click Me!")
myButton2 = Button(root, text="Click Me!", state=DISABLED)
myButton3 = Button(root, text="Click Me!", padx=50)
myButton4 = Button(root, text="Click Me!", pady=50)
myButton5 = Button(root, text="Click Me!", command=clickme)
myButton6 = Button(root, text="Click Me!", command=clickme, fg="white", bg="black")


# Using Pack Function
myButton.pack()
myButton2.pack()
myButton3.pack()
myButton4.pack()
myButton5.pack()
myButton6.pack()

# Using Grid Functions
# myButton.grid(row=0, column=0)

# Looping the system
root.mainloop()
