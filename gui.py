from tkinter import *
from tkcalendar import Calendar,DateEntry
import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import sys
import time
from datetime import datetime,date
import sqlite3

top=Tk()
g=StringVar()
c=StringVar()
g.set(0)
c.set(0)
sub=""
def nextclick():
    g1=g.get()
    c1=c.get()
    sub = c1
    if g1=="new":
        new_attendance(sub)
        top.destroy()
    else:
        update(sub)
        top.destroy()

def cancelclick():
    top.destroy()

def new_attendance(sub):
    datep = date.today()
    sqliteConnection = sqlite3.connect(str(sub) + '_attendance_report_' + str(datep) + '.db')
    cursor = sqliteConnection.cursor()
    print("Succesfully connected to Sqlite")
    cursor.execute("CREATE TABLE attendance(Name TEXT,PRN TEXT,time TEXT,Date TEXT)")

    cap = cv2.VideoCapture(0)

    names = []

    def enterData(z):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        dtoday = date.today()
        if z in names:
            pass
        else:
            Z = ".join(str(z))"
            sqlite_insert_query = """INSERT INTO attendance( Name,PRN,time,Date) VALUES (?,?,?,?) """
            record = (z[15:-1], z[2:15], current_time, dtoday)
            cursor.execute(sqlite_insert_query, record)
            sqliteConnection.commit()
            return names

    def checkData(data):
        data = str(data)
        if data in names:
            print('Already Present')
        else:
            print('\n' + data + '' + 'Present')
            enterData(data)

    while True:
        ret, frame = cap.read()
        decodedObject = pyzbar.decode(frame)
        for obj in decodedObject:
            checkData(obj.data)
            time.sleep(1)

        cv2.imshow('Frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('s'):
            cv2.destroyAllWindows()
            break


    cursor.close()
    sqliteConnection.close()

def update(sub):
    top2 = Tk()
    top2.title("date select")
    top2.configure(background="#087593")
    #top2.configure(background="black")
    l3=Label(top2,text="Select the Date for Attendance update",bg='#087593',font=('arial', 13))
    l3.grid(row=1)
    top2.geometry("400x400+450+100")
    cal = DateEntry(top2, selectmode='day',background='black',bordercolor='black',headersbackground='black',normalbackground='black',forebackground='white',
                normalforeground='white',headersforeground='white')
    cal.grid(row=2, column=0, padx=20, pady=30)
    d = cal.get_date()
    def my_upd():
        l1.config(text=cal.get_date())
    def ok():
        update2()
        top2.destroy()
    def update2():
        sqliteConnection = sqlite3.connect(str(sub) + '_attendance_report_' + str(d) + '.db')
        cursor = sqliteConnection.cursor()
        print("Succesfully connected to Sqlite")

        cap = cv2.VideoCapture(0)

        names = []

        def enterData(z):
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            dtoday = date.today()
            if z in names:
                pass
            else:
                Z = ".join(str(z))"
                sqlite_insert_query = """INSERT INTO attendance( Name,PRN,time,Date) VALUES (?,?,?,?) """
                record = (z[15:-1], z[2:15], current_time, dtoday)
                cursor.execute(sqlite_insert_query, record)
                sqliteConnection.commit()
                return names

        def checkData(data):
            data = str(data)
            if data in names:
                print('Already Present')
            else:
                print('\n' + data + '' + 'Present')
                enterData(data)

        while True:
            ret, frame = cap.read()
            decodedObject = pyzbar.decode(frame)
            for obj in decodedObject:
                checkData(obj.data)
                time.sleep(1)

            cv2.imshow('Frame', frame)

            if cv2.waitKey(1) & 0xFF == ord('s'):
                cv2.destroyAllWindows()
                break

        cursor.close()
        sqliteConnection.close()


    l1 = Label(top2, text='selected date', font=('arial', 14))
    l1.grid(row=4, column=0)
    b3 = Button(top2, text='Get date', command=lambda: my_upd(), bg="#003797", fg="white", font=('arial', 14))
    b3.grid(row=2, column=1)
    b4 = Button(top2, text='OK', command=ok, bg="#003797", fg="white", font=('arial', 14))
    b4.place(x=175, y=300)
    top2.mainloop()


top.title("AAQR")
top.configure(background="#087593")
#top.configure(background="black")
top.geometry("500x600+450+100")
top.maxsize(700,700)
l1=Label(top,text="ATTENDANCE AUTOMATION",font=('ALGERIAN',22),bg='#087593')
l1.place(x=55,y=10)


r1=Radiobutton(top,text="NEW ATTENDANCE",variable=g,value="new",bg='#087593',font=('Times New Roman',14,'bold'))
r1.place(x=40,y =80)

r2=Radiobutton(top,text="UPDATE EXISTING",variable=g,value="update",bg='#087593',font=('Times New Roman',14,'bold'))
r2.place(x=40,y =120)

l3=Label(top,text="Select subject",bg='#087593',font=('Times New Roman',14,'bold'))
r1.place(x=40,y =80)
l3.place(x=40,y=160)

ch1=Radiobutton(top,text="Data Structure",variable=c,value="ds",bg='#087593',font=('Times New Roman',14,'bold'))
r1.place(x=40,y =80)
ch1.place(x=70,y=200)
ch2=Radiobutton(top,text="Digital Logic Design",variable=c,value="dld",bg='#087593',font=('Times New Roman',14,'bold'))
r1.place(x=40,y =80)
ch2.place(x=70,y=240)
ch3=Radiobutton(top,text="Programming Logic Design ",variable=c,value="pld",bg='#087593',font=('Times New Roman',14,'bold'))
r1.place(x=40,y =80)
ch3.place(x=70,y=280)
ch4=Radiobutton(top,text="Python Programming ",variable=c,value="pp",bg='#087593',font=('Times New Roman',14,'bold'))
r1.place(x=40,y =80)
ch4.place(x=70,y=320)
ch5=Radiobutton(top,text="Discrete Mathematics ",variable=c,value="dms",bg='#087593',font=('Times New Roman',14,'bold'))
r1.place(x=40,y =80)
ch5.place(x=70,y=360)
ch6=Radiobutton(top,text="Linear Algebra ",variable=c,value="lait",bg='#087593',font=('Times New Roman',14,'bold'))
r1.place(x=40,y =80)
ch6.place(x=70,y=400)

b1=Button(top,text="NEXT",command=nextclick,bg="#003797",fg="white",font=('Times New Roman',14,'bold'))
r1.place(x=40,y =80)
b1.place(x=270,y=450)
b2=Button(top,text="Cancel",command=cancelclick,bg='#003797',font=('Times New Roman',14,'bold'),fg='#fffded')
r1.place(x=40,y =80)
b2.place(x=170,y=450)
top.mainloop()
