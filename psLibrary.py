#python standard library
# working with paths

from email.mime import image
from genericpath import isdir
from pathlib import Path
import smtpd

# path = Path("ecommerce/__init__.py")
# path.is_file()
# print(path.name)
# path = path.with_name("pythonStandardLibrary.txt")
# print(path.absolute())

# path2 = Path("ecommerce/__init__.py") 
# #using a generator object

# paths = [p for p in path2.iterdir() if p.is_dir()]
# print(paths)

# #working with files

path =Path("webdev4/file1.txt")
print(path.stat())

#to make time in human readable
from time import ctime
import shutil

# source = Path("webdev4/ecommerce/__init__.py")
# target = Path() /"__init__.py"
# shutil.copy(target, source)

print(ctime(path.stat().st_ctime))
print(path.read_text())

#working with zipfile
# from zipfile import ZipFile
# with ZipFile("files.zip", "w") as zip:
#     for path in Path("webdev4/ecommerce/").rglob("*.*"):
#         zip.write(path)
# with ZipFile("files.zip") as zip:
#     print(zip.namelist())
#     zip.extractall("extracted")

# working with csv files
import csv
#Project on csv
with open("data.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
   
    
#working with JSON files
#project on json
import json

# movies =[
#     {"id" : 1, "title" : "terminator", "year":1989},
#     {"id" : 2, "title" : "mr bean", "year":1999},
#     {"id" : 3, "title" : "jet li", "year":2000},
#     {"id" : 4, "title" : "tom and jerry", "year":1989},
#     {"id" : 5, "title" : "lucifer", "year":1997},
#     {"id" : 6, "title" : "sunday dagboru", "year":1999},
#     {"id" : 7, "title" : "terminator 2", "year":1980},
#     {"id" : 8, "title" : "terminator 3", "year":1981},
#     {"id" : 9, "title" : "rush hour 1", "year":1982},
#     {"id" : 10, "title" : "rush hour 2", "year":1983},
#     {"id" : 11, "title" : "rush hour 3", "year":1984}
# ]
# data = json.dumps(movies)
# print(movies)


#working with sqlite database
import sqlite3
movies =json.loads(Path("movies.json").read_text())
#connecting to a database
# with sqlite3.connect("db_movies") as connection:
#     command = "INSERT INTO Movies VALUES( ?, ?, ?)"
#     for movie in movies:
#         connection.execute(command, tuple(movie.values()))
#     connection.commit()

# print(movies)

with sqlite3.connect("db_movies") as connection:
    command = "SELECT * FROM Movies WHERE year > 1983"
    cursor =connection.execute(command)
    for row in cursor:
        print(row)
#cursor => an iterable object

#working with date and time
#simulating sending an email to 10,000 recipient

import time

def send_emails():
    for i in range(10000):
        pass

starttime = time.time()
send_emails()
endtime = time.time()
duration = endtime - starttime
print(duration)

#using datetime
from datetime import datetime, timedelta

dt = datetime(2000, 6, 1) + timedelta(days =1)
dt2 = datetime.now()
duration = dt2 -dt

print(f"my baby has stayed {duration} on earth")

# import webbrowser
# print("deployment completed")
# webbrowser.open("https://google.com")

#sending emails to customers based on their interest
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

message = MIMEMultipart()
message["from"] = "franklinnemeka@gmail.com"
message["to"] = "franklynchrys@gmail.com"
message["subject"] = "lUsing python to send emails this days"
message.attach(MIMEText("Body"))

with smtplib.SMTP(host ="smtp.gmail.com", port = 587 ) as smtp:
    #steps to follow
    smtp.ehlo() # greeting to the server
    smtp.starttls() # transport layer security mode
    smtp.login("franklinnemeka@gmail.com", "frankolin09@")
    smtp.send_message(message)
    print("sent ...")

