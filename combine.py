# OptionMenu (input)
# Entry (input)
# Button (input)
# Label (output)

from tkinter import *

top = Tk()

om = StringVar()
om.set("one")
option = OptionMenu(top, om, "one", "two", "three", "four")
option.pack()

E1 = Entry(top, bd =5)
# E1.pack(side = RIGHT)
E1.pack()

lab = StringVar()

def but_func(event):
    # print('but_func')
    om_value = om.get()
    entry_value = E1.get()

    # if om_value == 'MySQL', send query(determined by om_value and entry_value) to mysql

    # else send the query commsnds depend on om_value (switch cases)

    # get the query result(in the way determined by om_value and entry_value) from mysql

    # output to GUI
    lab.set(om_value + entry_value)


b = Button(top, text='my button')
b.bind("<Button-1>", but_func)
# b.place(x=100,y=20)
b.config( height = 1, width = 30)
b.pack()

lab.set('label initial content')
w = Label(top, textvariable=lab)
w.pack()

top.mainloop()