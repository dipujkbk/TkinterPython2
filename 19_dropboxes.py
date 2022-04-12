from tkinter import *
from PIL import Image,ImageTk

root=Tk()
root.title("main window")
root.iconbitmap("truck.ico")
root.geometry("400x400")

def show():
    my_label = Label(root,text=clicked.get()).pack()

mylist_option =["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
clicked = StringVar()
clicked.set(mylist_option[0]) # to set bydefault some selection 


drop =  OptionMenu(root,clicked, *mylist_option)
drop.pack()

mybutton = Button(root,text="show selection",command=show).pack()

root.mainloop()
