from tkinter import *
from tkinter import messagebox

root=Tk()
def popup():
    # messagebox.showinfo("This is my popup!","Hello world")
    #messagebox.showwarning("This is my popup!","Hello world")
    # messagebox.showerror("This is my popup!","Hello world")
    # messagebox.askquestion("This is my popup!","Hello world")
    # messagebox.askokcancel("This is my popup!","Hello world")
    response = messagebox.askyesno("This is my popup!","Hello world")
    if response==1:
        Label(root,text='You clicked Yes').pack()
    if response==0:
        Label(root,text='You clicked No').pack()


Button(root,text="Popup", command=popup).pack()
root.mainloop()





































