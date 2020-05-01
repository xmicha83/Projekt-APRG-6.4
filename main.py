import sqlite3
from knihovna import *
import re
from sklearn.metrics.pairwise import cosine_similarity
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
readalllines("combined_data_1.txt", 1)
readalllines("combined_data_2.txt", 1)
readalllines("combined_data_3.txt", 1)
readalllines("combined_data_4.txt", 1)
readalllines("movie_titles.csv", 1)
curr = conn.cursor()
curr.execute("SELECT * FROM HODNOCENI")
print(curr.fetchall())


#rating.mean() = stredne hodnoty hodnotení používateľa aby sme sa vyhli nulovým (žiadnym) hodnoteniam
#item_similarity = použijeme kosínovu podobnosť
#def get_similar_movies(movie_name, user_similarity):
    #similar_score = item_similarity(movie_name)*(user_rating - rating.mean()) --- filmy zoradíme podľa podobnosti
#zadefinujeme používateľa, pre ktorého hľadáme podobné filmy
#premennú similar_movies nám zobrazuje tabuľka
#for movie, rating in používateľ:
    #similar_movies = similar_movies.append(get_similar_movies(movie, rating))


def main():


if __name__ == "__main__":
    main()
