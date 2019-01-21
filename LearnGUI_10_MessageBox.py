from tkinter import *
import tkinter.messagebox

root = Tk()
tkinter.messagebox.showinfo("Error", "Your Computer is Working Wrong")
ans = tkinter.messagebox.askquestion("Question", "Are You Good Boy?")

if ans == 'yes':
    print("I Love You")

root.mainloop()