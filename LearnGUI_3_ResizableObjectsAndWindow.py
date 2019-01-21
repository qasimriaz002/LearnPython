from tkinter import *

root = Tk()

label1 = Label(root, text = "Label - 1", bg = "red", fg = "white")
label1.pack()
label2 = Label(root, text = "Label - 2", bg = "blue", fg = "white")
label2.pack(fill = X)
label3 = Label(root, text = "Label - 3", bg = "green", fg = "white")
label3.pack(side = LEFT, fill = Y)
label4 = Label(root, text = "Label - 4", bg = "Black", fg = "white")
label4.pack(side = BOTTOM, fill = BOTH)

root.mainloop()