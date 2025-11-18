import tkinter
m = tkinter.Tk()
m.geometry("400x300")

l = tkinter.Label(m, text="Hello World")
l.pack()

e1 = tkinter.Entry(m)
e1.pack()

def printIt(event = None):
    textbox.insert(tkinter.END, e1.get() + "\n")

button = tkinter.Button(m, text="Click Me", command=printIt)
m.bind('<Return>', printIt)
button.pack()

textbox = tkinter.Text(m, height=10, width=30)
textbox.pack()

m.mainloop()
