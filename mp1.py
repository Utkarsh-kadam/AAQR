import pyqrcode
import png
f=open('student.txt','r')
lines=f.read().split("\n")
print(lines)

for i in range(0,len(lines)):
    url = pyqrcode.create(lines[i])
    url.png(str(lines[i]+'.png'), scale=8)