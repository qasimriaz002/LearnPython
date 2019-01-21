from tkinter import *

root = Tk()

def func():
    print("Hello Function Is Called Directly ")

def funcLeftClick(event):
    print("Hello Function Is Called Using The Event Left Click On Mouse")

def funcScrollClick(event):
    print("Hello Function Is Called Using The Event Scroll Click On Mouse")

def funcRigthClick(event):
    print("Hello Function Is Called Using The Event Right Click On Mouse")

button1 = Button(root, text = "Call Function Directky", command = func)
button1.pack()

button2 = Button(root, text = "Call Function Using Event")
button2.pack()

button2.bind("<Button-1>", funcLeftClick) #On Clicking the Left Button Mouse
button2.bind("<Button-2>", funcScrollClick) #On Clicking the Scroll Button on Mouse
button2.bind("<Button-3>", funcRigthClick) #On Clickong the Rigth Button on Mouse

root.mainloop()