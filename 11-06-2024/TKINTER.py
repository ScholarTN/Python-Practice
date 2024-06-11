#import all the classes,functions and variables from tkinter
from tkinter import *

root=Tk()   #create a root widget by calling the Tk()
            #Thhis automatically creates a graphical window with title bar, minimize, maximize and close buttons.

X = Label(root,text="Hello, world!") #CREATING a LABEL widget as a child to the root window
                                     #Default text set to Helo world!
#A label window can display either a text or icon or other image

X.pack()     #Calling the pack method
             #Tells the widget to size itself to fit the given text and make itself visible
             #Tells the geometry manager to put widgets in same row or column

root.mainloop()  #The application window does not appear before you enter the main loop.
                 # This method says to take all the widgets and objects created, render them on our screen
                  #AND respond to any interactions
#The program stays in loop until until we close the window


