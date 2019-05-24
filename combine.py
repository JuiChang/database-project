# OptionMenu (input)
# Entry (input)
# Button (input)
# Label (output)

from tkinter import *

top = Tk()

# row 1
dlab1_str = StringVar()
dlab1_str.set('Cram School Database')
dlab1 = Label(top, textvariable=dlab1_str, )
dlab1.config(font=("Courier", 25), bg='SkyBlue1')
dlab1.grid(row=0, columnspan=2, ipady=30, sticky='nsew')

# row 2
dlab2_str = StringVar()
dlab2_str.set('Options')
dlab2 = Label(top, textvariable=dlab2_str)
dlab2.config(font=("Courier", 20), bg='DarkSeaGreen1')
# dlab2.pack(side = LEFT)
dlab2.grid(row=1, column=0, sticky='nsew')

om_str = StringVar()
om_str.set("one")
om = OptionMenu(top, om_str, "one", "two", "three", "four")
om.config(width=60)
# om.pack(side = RIGHT)
om.grid(row=1, column=1, sticky='nsew')

# row 3
dlab3_str = StringVar()
dlab3_str.set('KeyWords')
dlab3 = Label(top, textvariable=dlab3_str)
dlab3.config(font=("Courier", 20), bg='hot pink')
# dlab3.pack(side = LEFT)
dlab3.grid(row=2, column=0, sticky='nsew')


text = Text(top)
text.config(width=85, highlightbackground='green')
# text.pack(side=RIGHT)
text.grid(row=2, column=1, sticky='nsew')


lab_str = StringVar()

def but_func(event):
    # print('but_func')
    om_value = om_str.get()
    # entry_value = e.get()
    text_value = text.get("1.0",END)

    # if om_value == 'MySQL', send query(determined by om_value and entry_value) to mysql

    # else send the query commsnds depend on om_value (switch cases)

    # get the query result(in the way determined by om_value and entry_value) from mysql

    # output to GUI
    lab_str.set(om_value + '\n' + text_value)

# row 4
b = Button(top, text='Search', bg='yellow')
b.bind("<Button-1>", but_func)
# b.place(x=100,y=20)
# b.config( height = 2, width = 80, bg='yellow')
b.grid(row=3, columnspan=2, sticky='nsew')


# row 5
dlab4_str = StringVar()
dlab4_str.set('Query Result')
dlab4 = Label(top, textvariable=dlab4_str)
dlab4.config(font=("Courier", 20))
dlab4.grid(row=4, columnspan=2, ipady=20, sticky='nsew')


# row 6
lab_str.set('no content')
lab = Label(top, textvariable=lab_str)
lab.grid(row=5, columnspan=2, sticky='nsew')

top.mainloop()