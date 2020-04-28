films = []


class rating:
    def __init__(self, user_id, value, date):
        self.user_id = user_id
        self.value = value
        self.date = date


class film:
    def __init__(self, id, year, name):
        self.id = id
        self.year = year
        self.name = name
        # v pripade pristupu podla userov prerobit na dict. key=user_id, value = ( value, date ) / (rating)
        self.ratings = []

    def add_rating(self, rating):
        self.ratings.append(rating)


class reader:
    def __init__(self, data_files, movie_titles):
        self.data_files = []
        for file in data_files:
            with open(file, "r") as data:
                for line in data.readlines():
                    self.data_files.append(line)
                # print(self.data_files)
        self.movie_titles = open(movie_titles, "r").readlines()
        self.i = 0
        self.data_len = len(self.data_files)

    def load_all_films(self):
        for new_film in self.movie_titles:
            new_film = new_film.split(",")
            self.load_next_film(
                film(int(new_film[0]), new_film[1], new_film[2].strip("\n")))

    def load_next_film(self, new_film):
        # print(new_film.name)
        k = True
        while self.i < self.data_len:
            # print(self.i)
            data = str(self.data_files[self.i]).split(',')

            if(len(data) == 1):
                if(k):
                    k = False
                    self.i += 1
                    if(int(data[0].strip(":\n")) != new_film.id):
                        print("ERROR: mismatch in id:", data)
                        return
                else:
                    films.append(new_film)
                    return
            if(len(data) == 3):
                new_film.add_rating(
                    rating(data[0], data[1], data[2].strip("\n")))
                self.i += 1
        films.append(new_film)
        return


my_reader = reader(["combined_data_1.txt", "combined_data_2.txt",
                    "combined_data_3.txt", "combined_data_4.txt"], "movie_titles.csv")
my_reader.load_all_films()
for film in films:
    print(film.name, film.year, film.id, "\n", len(film.ratings))
    if(film.id == 115):
        break
