# Attendance Automation using QR Code

This project provides an attendance automation system using QR code technology. It allows for the easy and efficient recording of attendance in various subjects or classes by scanning QR codes with a webcam or camera.

## Features

- Automated attendance recording using QR code scanning
- Supports both new attendance recording and updating existing records
- Subject selection for organizing attendance data
- Database storage for attendance records
- Real-time date selection for updating existing attendance
- User-friendly graphical user interface (GUI)

## Dependencies
The following dependencies are used in this project:
1. [tkinter](https://docs.python.org/3/library/tkinter.html)
2. [cv2](https://pypi.org/project/opencv-python/)
3. [pyzbar](https://pypi.org/project/pyzbar/)
4. [sqlite3](https://docs.python.org/3/library/sqlite3.html)

## Installation

To use the Attendance Automation system, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/Utkarsh-kadam/AAQR.git
```
2.Run the application:
```bash
python gui.py
```
4.Select the attendance type (new or update) and choose the subject.

5. If selecting "New Attendance," the system will create a new attendance report for the specified subject and start scanning QR codes to record attendance.

6. If selecting "Update Existing," the system will prompt you to select the date for updating the attendance records. Once selected, the system will scan QR codes and update the attendance for the chosen date and subject.

7. The attendance records will be stored in a SQLite database file with the subject name and the current date.

## Screenshot
![Screenshot (1439)](https://github.com/Utkarsh-kadam/AAQR/assets/99534647/77037566-3928-4efa-9133-f0e569fce011)
