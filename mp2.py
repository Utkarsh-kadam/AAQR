sub=input("Enter subject Name:")
import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import sys
import time
from datetime import datetime,date
import sqlite3
datep=date.today()

sqliteConnection = sqlite3.connect(str(sub)+'_attendance_report_'+str(datep)+'.db')
cursor=sqliteConnection.cursor()
print("Succesfully connected to Sqlite")
cursor.execute("CREATE TABLE attendance(Name TEXT,PRN TEXT,time TEXT,Date TEXT)")


cap =cv2.VideoCapture(0)

names=[]

fob=open('attendance.txt','a+')
def enterData(z):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    dtoday = date.today()
    if z in names:
        pass
    else:
        names.append(z)
        Z=".join(str(z))"
        fob.write(z+' ')
        fob.write(current_time+'\n')
        sqlite_insert_query = """INSERT INTO attendance( Name,PRN,time,Date) VALUES (?,?,?,?) """
        record=(z[15:-1],z[2:15],current_time,dtoday)
        cursor.execute(sqlite_insert_query,record)
        sqliteConnection.commit()
        return names

def checkData(data):
    data = str(data)
    if data in names:
        print('Already Present')
    else:
        print('\n'+data+''+'Present')
        enterData(data)


while True:
    ret,frame=cap.read()
    decodedObject=pyzbar.decode(frame)
    for obj in decodedObject:
        checkData(obj.data)
        time.sleep(1)

    cv2.imshow('Frame',frame)

    if cv2.waitKey(1)& 0xFF==ord('s'):
        cv2.destroyAllWindows()
        break

fob.close()
cursor.close()
sqliteConnection.close()