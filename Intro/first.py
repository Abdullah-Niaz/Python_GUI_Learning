from tkinter import *\

#! Main window  object name 
Box = Tk()
frame = Frame(Box)
frame.pack()

#!  Giving the title to the window
Box.title("First Program")


#! Label is what output will be
#! show on the window
label = Label(frame, text="Hello World").pack(side=TOP)
button = Button(frame, text="Hello", fg='blue',bg="green").pack()

#! calling mainloop method which is used
#! when your application is ready to run
#! and it tells the code to keep displaying
frame.mainloop()