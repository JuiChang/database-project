# OptionMenu (input)
# Entry (input)
# Button (input)
# Label (output)

from tkinter import *

top = Tk()

frame1 = Frame(top, width=800, height=100, bg='DarkSeaGreen1')
frame1.pack()
frame1.pack_propagate(0)
frame2 = Frame(top, width=800, height=100, bg='hot pink')
frame2.pack()
frame2.pack_propagate(0)
frame3 = Frame(top, width=800, height=100, bg='SkyBlue1')
frame3.pack()
frame3.pack_propagate(0)
frame4 = Frame(top, width=800, height=100, bg='yellow')
frame4.pack()
frame4.pack_propagate(0)
frame5 = Frame(top, width=800, height=100, bg='thistle1')
frame5.pack()
frame5.pack_propagate(0)

# frame 1
dlab1_str = StringVar()
dlab1_str.set('Cram School Database')
dlab1 = Label(frame1, textvariable=dlab1_str)
dlab1.config(font=("Courier", 20), width=60, height=3, bg='DarkSeaGreen1')
dlab1.pack()

# frame 2
dlab2_str = StringVar()
dlab2_str.set('Search Tool')
dlab2 = Label(frame2, textvariable=dlab2_str)
dlab2.config(font=("Courier", 20))
# dlab2.pack(side = LEFT)
dlab2.grid(row=0, column=0)

om_str = StringVar()
om_str.set("one")
om = OptionMenu(frame2, om_str, "one", "two", "three", "four")
om.config(width=60)
# om.pack(side = RIGHT)
om.grid(row=0, column=1)

# frame 3
dlab3_str = StringVar()
dlab3_str.set('KeyWords')
dlab3 = Label(frame2, textvariable=dlab3_str)
dlab3.config(font=("Courier", 20))
dlab3.pack(side = LEFT)
dlab3.grid(row=1, column=0)

# e = Entry(frame3, bd=5) #?
# e.pack(side = RIGHT)
text = Text(frame2)
text.config(width=85)
text.pack(side=RIGHT)
text.grid(row=1, column=1)


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

# frame 4
b = Button(frame4, text='Search', bg='yellow')
b.bind("<Button-1>", but_func)
# b.place(x=100,y=20)
# b.config( height = 2, width = 80, bg='yellow')
b.pack(fill=BOTH)


# frame 5
lab_str.set('no content')
lab = Label(frame5, textvariable=lab_str)
lab.pack(fill=BOTH)

top.mainloop()