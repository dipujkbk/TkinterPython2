from tkinter import *


root= Tk()

myframe = LabelFrame(root,text='This is my frame',padx=15,pady=15) # this is padding inside the frame
myframe.pack(padx=50,pady=50)# this is padding outside the frame from the main container # here we use pack

b1 = Button(myframe,text='Dont click me')
b2 = Button(myframe,text='Dont click here')
b1.grid(row=0,column=0) # inside the frame we can use grid i.e here we can use pack in frame and grid inside it or we can use pack also here
b2.grid(row=1,column=0)

root.mainloop()