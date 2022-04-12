from tkinter import *
from PIL import Image,ImageTk

root=Tk()
root.title("main window")
root.iconbitmap("truck.ico")

top = Toplevel()
top.title("my second window")
my_img = ImageTk.PhotoImage(Image.open("dog-img.jpg"))
my_label = Label(top,image=my_img).pack()

mainloop()