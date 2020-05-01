import sqlite3
from knihovna import *
import re
conn = sqlite3.connect('databaze.db')
print("Opened database successfully")


def createdb():

    conn.execute('''CREATE TABLE HODNOCENI
            (FilmID INT PRIMARY KEY NOT NULL,
            HodID INT NOT NULL,
            USerID INT NOT NULL,
            Date DATE)''')

    conn.execute('''CREATE TABLE FILMY
             (FilmID INT PRIMARY KEY NOT NULL,
             Nazev char(50) NOT NULL,
             Date DATE)''')

    conn.commit()
    return True


createdb()
readalllines("combined_data_2.txt", 1)
curr = conn.cursor()
curr.execute("SELECT * FROM HODNOCENI")
print(curr.fetchall())
