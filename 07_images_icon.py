from tkinter import *
from PIL import ImageTk,Image



root= Tk()
root.title('dog-dog')
root.iconbitmap('truck.ico')


myimg = ImageTk.PhotoImage(Image.open('dog-img.jpg')) # define the image
mylabel = Label(image=myimg) # puting into widget
mylabel.pack() # puting into window



button_quit = Button(root, text='Exit Program', command=root.quit)
button_quit.pack()

root.mainloop()