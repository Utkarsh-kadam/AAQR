from tkinter import *
from tkcalendar import DateEntry
top2 = Tk()
top2.configure(background="#087593")
top2.geometry("400x400+450+100")
cal = DateEntry(top2, selectmode='day',background='black',bordercolor='black',headersbackground='black',normalbackground='black',forebackground='white',
                normalforeground='white',headersforeground='white')
cal.grid(row=1, column=1, padx=20, pady=30)

def my_upd():
    l1.config(text=cal.get_date())
    print(cal.get_date())
def ok():
    top2.destroy()

l1 =Label(top2, text='selected date',bg="#087593",font=('arial',14))
l1.grid(row=4, column=1)
b3 = Button(top2, text='Get date', command=lambda: my_upd(),bg="#003797",fg="white",font=('arial',14))
b3.grid(row=1, column=2)
b4 = Button(top2, text='OK', command=ok,bg="#003797",fg="white",font=('arial',14))
b4.grid(row=6,column=2)
top2.mainloop()