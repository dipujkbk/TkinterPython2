from tkinter import *
from PIL import Image,ImageTk

root=Tk()
root.geometry("400x400")

root.iconbitmap("truck.ico")

var1 = IntVar()
var2 = StringVar()

c1 = Checkbutton(root,text="Check this box 1",variable= var1)
c1.pack()

c2 = Checkbutton(root,text="Check this box 2",variable= var2, onvalue="On",offvalue= "Off")
c2.deselect() # bydefault it is selected so to deselect 
c2.pack()

def show():
    mylabel = Label(root,text=var1.get()).pack()
    mylabel1 = Label(root,text=var2.get()).pack()


mybutton = Button(root, text="Show selsection", command=show).pack()


root.mainloop()