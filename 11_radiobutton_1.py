from tkinter import *

root = Tk()

v = IntVar()
v.set(2)

def clicked(value):
    mylabel = Label(root,text=value)
    mylabel.pack()

Radiobutton(root,text="python",variable=v,value=1,command=lambda: clicked(v.get())).pack()
Radiobutton(root,text="c++",variable=v,value=2,command=lambda: clicked(v.get())).pack()
Radiobutton(root,text="java",variable=v,value=3,command=lambda: clicked(v.get())).pack()

root.mainloop()