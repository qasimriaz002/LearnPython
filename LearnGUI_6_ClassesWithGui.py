from tkinter import *


class GuiClass:

    def __init__(self, master):
        frame1 = Frame(master)
        frame1.pack()

        self.button1 = Button(frame1, text = "Click to Print", command = self.showMessage)
        self.button2 = Button(frame1, text = "Quit", command = frame1.quit)

        self.button1.pack(side = LEFT)
        self.button2.pack(side = LEFT)

    def showMessage(self):
        print("Finally We Called It Using The Classe")


root = Tk()
myGuiClass = GuiClass(root)
root.mainloop()
