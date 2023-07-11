from tkinter import *\

#! Main window  object name 
Box = Tk()

#!  Giving the title to the window
Box.title("First Program")


#! Label is what output will be
#! show on the window
label = Label(Box, text="Hello World").pack()

#! calling mainloop method which is used
#! when your application is ready to run
#! and it tells the code to keep displaying
Box.mainloop()