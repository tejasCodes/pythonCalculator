import tkinter
from tkinter import *

c = tkinter.Tk()
c.title('python calculator');
	
	
# Event listners
def btn_1_click():
	soltext = "dd"
	print(soltext)

# Member Variable
soltext = tkinter.StringVar()
soltext = 's'
	
# UI creation
textWindow = tkinter.Entry(c, textvariable=soltext)
textWindow.grid(row=0, columnspan=4, sticky= tkinter.W + tkinter.E)
tkinter.Label(c, text="welcome ...").grid(row=1, columnspan=4, sticky= tkinter.W + tkinter.E)
tkinter.Button(c, text='1', width=5, height=2, command=btn_1_click).grid(row=2, column=0)
tkinter.Button(c, text='2', width=5, height=2).grid(row=2, column=1)
tkinter.Button(c, text='3', width=5, height=2).grid(row=2, column=2)
tkinter.Button(c, text='+', width=5, height=2).grid(row=2, column=3)
tkinter.Button(c, text='4', width=5, height=2).grid(row=3, column=0)
tkinter.Button(c, text='5', width=5, height=2).grid(row=3, column=1)
tkinter.Button(c, text='6', width=5, height=2).grid(row=3, column=2)
tkinter.Button(c, text='-', width=5, height=2).grid(row=3, column=3)
tkinter.Button(c, text='7', width=5, height=2).grid(row=4, column=0)
tkinter.Button(c, text='8', width=5, height=2).grid(row=4, column=1)
tkinter.Button(c, text='9', width=5, height=2).grid(row=4, column=2)
tkinter.Button(c, text='/', width=5, height=2).grid(row=4, column=3)
tkinter.Button(c, text='.', width=5, height=2).grid(row=5, column=0)
tkinter.Button(c, text='0', width=5, height=2).grid(row=5, column=1)
tkinter.Button(c, text='±', width=5, height=2).grid(row=5, column=2)
tkinter.Button(c, text='*', width=5, height=2).grid(row=5, column=3)
textWindow.focus()
c.bind('<Return>', btn_1_click)
c.mainloop()

