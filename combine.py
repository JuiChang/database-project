# OptionMenu (input)
# Entry (input)
# Button (input)
# Label (output)

from tkinter import *


top = Tk()

labelout = StringVar()

om_value = "om initial"
entry_value = "entry initial"

def om_func(value):
    global om_value
    om_value = value
    print(om_value)

def entry_func(e):
    global entry_value 
    entry_value = e.widget.get()
    print(entry_value)
    print('1')




omout = StringVar()
omout.set("one") # initial value
option = OptionMenu(top, omout, "one", "two", "three", "four", command=om_func)
option.pack()

E1 = Entry(top, bd =5)
# E1.pack(side = RIGHT)
# E1.bind("<Key>", entry_func) 
E1.pack()

def but_func(event):
    print(omout.get())
    print(E1.get())
    print('1')

    # print('but_func')

    # if om_value == 'MySQL', send query(determined by om_value and entry_value) to mysql

    # else send the query commsnds depend on om_value (switch cases)

    # get the query result(in the way determined by om_value and entry_value) from mysql

    # output to GUI
    labelout.set(entry_value)
    print('2')

b = Button(top, text='bbutton')
b.bind("<Button-1>", but_func)
# b.place(x=100,y=20)
b.pack()

labelout.set('blue sky')
w = Label(top, textvariable=labelout)
w.pack()

top.mainloop()