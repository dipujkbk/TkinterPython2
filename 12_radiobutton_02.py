from tkinter import *

root = Tk()


Modes = [
    ("Pepperoni","90"),
    ("Cheese","120"),
    ("Mushroom","63"),
    ("Onion","78"),
    ("Chilli","99")
]

pizza = StringVar()
pizza.set("63")

def clicked(value):
    mylabel = Label(root,text=value)
    mylabel.pack()

for pname,pprice in Modes:
    Radiobutton(root,text=pname,variable=pizza,value=pprice).pack(anchor=W)



b =Button(root,text="click me to get the price",command=lambda: clicked(pizza.get())).pack()

root.mainloop()