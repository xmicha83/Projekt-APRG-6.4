import re
import sqlite3
conn = sqlite3.connect("databaze.db")


def readalllines(filename, mod): #načtení dat do tabulek v databázi
    try:
        f = open(filename, 'r')
    except:
        print("error1")
        exit(1)

    for line in f:
        print(line)
        if mod == 1:
            film_id = -1
            if re.match('\\d+:', line):
                film_id = line.split(':')[0]
            elif re.match('(\\d+),(\\d),(\\d+-\\d+-\\d+)', line):
                if film_id == -1:
                    exit(1)
                data = line.split(',')
                var = str(film_id)
                conn.execute("INSERT INTO HODNOCENI (FilmID, UserID, HodID, Date) "
                             "VALUES ("+var+","+data[0]+","+data[1]+","+data[2]+")")
            else:
                print("error2")
                exit(1)
        else:
            if re.match('(\\d+),(\\d+),(.*)', line):
                l = []
                l = line.split(',')
                conn.execute("INSERT INTO FILMY (FilmID, Nazev, Date) VALUES (" + l[0] + "," + l[1] + "," + l[2] + ")")
            else:
                print("error3")
                exit(1)



