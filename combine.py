# OptionMenu (input)
# Entry (input)
# Button (input)
# Label (output)

from tkinter import *
import MySQLdb

# 連接 MySQL 資料庫
db = MySQLdb.connect(host="localhost",
    user="root", passwd="rootroot", db="cramschool")
cursor = db.cursor(MySQLdb.cursors.DictCursor)


top = Tk()

# row 1
dlab1_str = StringVar()
dlab1_str.set('Cram School Database')
dlab1 = Label(top, textvariable=dlab1_str, )
dlab1.config(font=("Courier", 25), bg='SkyBlue')
dlab1.grid(row=0, columnspan=2, ipady=30, sticky='nsew')

# row 2
dlab2_str = StringVar()
dlab2_str.set('Options')
dlab2 = Label(top, textvariable=dlab2_str)
dlab2.config(font=("Courier", 20), bg='PaleGreen3')
dlab2.grid(row=1, column=0, padx=2, pady=2, sticky='nsew')

om_str = StringVar()
om_str.set("MySQL")
om = OptionMenu(top, om_str, "MySQL", 
                            "SELECT () FROM () WHERE (). Format: (), (), ()",
                            "UPDATE StudentPhone by StudentID. Format: StudentID, StudentPhone",
                            "INSERT STUDENT. Format: StudentID, StudentName, StudentPhone",
                            "DELETE COURSE by CourseID. Format: CourseID",
                            "Names of the employees whose id is IN MANAGE (i.e. all managers' names).",
                            "Names of the employees whose id is NOT IN ADVERTISE",
                            "Names of the university whose id EXISTS in ADVERTISE",
                            "Names of the courses whose id NOT EXISTS in SELL",
                            "Name and hours of the Course with MAX hours",
                            "Name and hours of the Course with MIN hours",
                            "AVG sell price of a course",
                            "COUNT of employees",
                            "SUM of the hours of all courses",
                            "pairs of (EmployeeName, StudentName), HAVING COUNT > 1 in SELL"
                            )
om.config(width=60)
om.grid(row=1, column=1, sticky='nsew')

# row 3
dlab3_str = StringVar()
dlab3_str.set('KeyWords')
dlab3 = Label(top, textvariable=dlab3_str)
dlab3.config(font=("Courier", 20), bg='PaleGreen3')
dlab3.grid(row=2, column=0, padx=2, pady=2, sticky='nsew')

text = Text(top)
text.config(height=15, highlightbackground='green')
text.grid(row=2, column=1, sticky='nsew')


# row 6
frame = Frame(top)
frame.grid(row=5, columnspan=2, sticky='nsew')
secdf = Frame(frame)
secdf.pack()



# "COUNT of employees",
# "SUM of the hours of all courses",
# "pairs of (EmployeeName, StudentName), HAVING COUNT > 1 in SELL"

def but_func(event):
    global secdf
    om_value = om_str.get()
    text_value = text.get("1.0",END)
    exception = 0

    try:
        if om_value == 'MySQL':    
            cursor.execute(text_value)       
            db.commit()   

        elif om_value == 'SELECT () FROM () WHERE ()':
            li = [x.strip() for x in text_value.split(',')]
            cursor.execute('SELECT ' + li[0] + 
                            ' FROM ' + li[1] + 
                            ' WHERE ' + li[2] + ';')

        elif om_value == "UPDATE StudentPhone by StudentID. Format: StudentID, StudentPhone":
            li = [x.strip() for x in text_value.split(',')]
            cursor.execute('UPDATE STUDENT SET StudentPhone=' + li[1] + 
                            'WHERE StudentID=' + li[0] + ';')
            db.commit()

        elif om_value == "INSERT STUDENT. Format: StudentID, StudentName, StudentPhone":
            li = [x.strip() for x in text_value.split(',')]
            cursor.execute('INSERT INTO STUDENT (StudentID, StudentName, StudentPhone) VALUES (' + 
                            li[0] + ',' + li[1] + ',' + li[2] + ')' + ';')
            db.commit()

        elif om_value == "DELETE COURSE by CourseID. Format: CourseID":
            li = [x.strip() for x in text_value.split(',')]
            cursor.execute('DELETE FROM COURSE WHERE CourseID=' + li[0] + ';')
            db.commit()

        elif om_value == "Names of the employees whose id is IN MANAGE (i.e. all managers' names).":
            cursor.execute("""SELECT E.EmployeeName 
                                FROM EMPLOYEE E
                                WHERE E.EmployeeID IN (SELECT M.EmployeeID
                                                        FROM MANAGE M)""")
            
        elif om_value == "Names of the employees whose id is NOT IN ADVERTISE":
            cursor.execute("""SELECT E.EmployeeName 
                                FROM EMPLOYEE E
                                WHERE E.EmployeeID NOT IN (SELECT A.EmployeeID
                                                        FROM ADVERTISE A);""")
        
        elif om_value == "Names of the university whose id EXISTS in ADVERTISE":
            cursor.execute("""SELECT U2.UniversityName
                                FROM UNIVERSITY_1 U1, UNIVERSITY_2 U2 
                                WHERE U1.UniversityAddress = U2.UniversityAddress
                                AND EXISTS (SELECT *
                                            FROM ADVERTISE A
                                            WHERE A.UniversityID = U1.UniversityID);""")

        elif om_value == "Names of the courses whose id NOT EXISTS in SELL":
            cursor.execute("""SELECT C.CourseName
                                FROM Course C
                                WHERE NOT EXISTS (SELECT *
                                                FROM SELL S
                                                WHERE C.CourseID = S.CourseID);""")

        elif om_value == "Name and hours of the Course with MAX hours":
            cursor.execute("""SELECT CourseName, Hours
                                FROM COURSE
                                WHERE Hours = (SELECT MAX(Hours) FROM COURSE);""")
        
        elif om_value == "Name and hours of the Course with MIN hours":
            cursor.execute("""SELECT CourseName, Hours
                                FROM COURSE
                                WHERE Hours = (SELECT MIN(Hours) FROM COURSE);""")

        elif om_value == "AVG sell price of a course":
            cursor.execute("""SELECT AVG(Price)
                                FROM SELL;""")
        
        elif om_value == "COUNT of employees":
            cursor.execute("""SELECT COUNT(*)
                                FROM EMPLOYEE;""")

        elif om_value == "SUM of the hours of all courses":
            cursor.execute("""SELECT SUM(Hours)
                                FROM COURSE;""")

        elif om_value == "pairs of (EmployeeName, StudentName), HAVING COUNT > 1 in SELL":
            cursor.execute("""SELECT E.EmployeeName, ST.StudentName
                                FROM SELL S, EMPLOYEE E, STUDENT ST
                                WHERE S.EmployeeID = E.EmployeeID
                                AND S.StudentID = ST.StudentID
                                GROUP BY S.EmployeeID, S.StudentID
                                HAVING COUNT(*)>1;""")
            

    except (MySQLdb.Error, MySQLdb.Warning) as e:
            exception = 1
            print(e)
    
    

    if exception:
        lab_str = StringVar()
        lab_str.set("Query Failed")
        b = Label(secdf, textvariable=lab_str)
        b.pack()
        return

    results = cursor.fetchall()
    secdf.destroy()
    secdf = Frame(frame)
    secdf.pack()
    if len(results):
        num_row = len(results) + 1
        num_col = len(results[0])
        col_names = list(results[0].keys())
        for j in range(num_col):
            lab_str = StringVar()
            lab_str.set(col_names[j])
            b = Label(secdf, textvariable=lab_str)
            b.grid(row=0, column=j)
        for i in range(num_row - 1):
            for j in range(num_col):
                values = list(results[i].values())
                lab_str = StringVar()
                lab_str.set(values[j])
                b = Label(secdf, textvariable=lab_str)
                b.grid(row=i+1, column=j)
    
    

# row 4
b = Button(top, text='Query', bg='yellow')
b.bind("<Button-1>", but_func)
b.config(height = 2)
b.grid(row=3, columnspan=2, sticky='nsew')


# row 5
dlab4_str = StringVar()
dlab4_str.set('Query Result')
dlab4 = Label(top, textvariable=dlab4_str)
dlab4.config(font=("Courier", 20), bg='SkyBlue')
dlab4.grid(row=4, columnspan=2, ipady=20, sticky='nsew')


top.mainloop()