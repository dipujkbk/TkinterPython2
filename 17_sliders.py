from tkinter import *
from PIL import Image,ImageTk

root=Tk()
root.geometry("400x400")

root.iconbitmap("truck.ico")

vertical = Scale(root,from_= 0, to=400)
vertical.pack()
horizontal = Scale(root,from_=0, to=400, orient=HORIZONTAL)
horizontal.pack()

def slide():
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))

Button(root,text="resize the window",command=slide).pack()


mainloop()