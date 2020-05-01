import sqlite3
from knihovna import *
import re
conn = sqlite3.connect('databaze.db')
print("Opened database successfully")


def createdb(): #vytvoření tabulek v databázi

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
readalllines("combined_data_1.txt", 1)
readalllines("combined_data_2.txt", 1)
readalllines("combined_data_3.txt", 1)
readalllines("combined_data_4.txt", 1)
readalllines("movie_titles.csv", 1)

