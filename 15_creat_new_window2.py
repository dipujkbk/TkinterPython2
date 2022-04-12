from tkinter import *
from PIL import Image,ImageTk

root=Tk()
root.title("main window")
root.iconbitmap("truck.ico")

def open():
    global my_img # if i didn't declare it then my_img will not be displayed on the second window
    top = Toplevel()
    top.title("my second window")
    my_img = ImageTk.PhotoImage(Image.open("dog-img.jpg"))
    my_label = Label(top,image=my_img).pack()
    btn = Button(top,text="close window",command=top.destroy).pack()

btn = Button(root,text="Open second window",command=open).pack()

mainloop()