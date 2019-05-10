import tkinter

c = tkinter.Tk()
c.title('python calculator');
	
# UI creation
tkinter.Entry(c).grid(row=0, columnspan=4, sticky= tkinter.W + tkinter.E)
tkinter.Label(c, text="welcome ...").grid(row=1, columnspan=4, sticky= tkinter.W + tkinter.E)
tkinter.Button(c, text='1', width=5, height=2).grid(row=2, column=0)
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
c.mainloop()


