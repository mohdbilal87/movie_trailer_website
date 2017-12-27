import os
import csv
import media
import fresh_tomatoes

# initializing an empty list. will be populated with movie data read from a csv file
movies = []

# reading the csv file and populating the empty list
# since the storyline can have commans, the csv file is actually pipe separated hence the "register_dialect" method
csv.register_dialect('pipes', delimiter='|')
current_dir = os.getcwd()
f = open(current_dir + "/movie_metadata.csv", 'r')

try:
    reader = csv.reader(f, dialect='pipes')
    for row in reader:
        # calling the constructor to initilaze an object and populating
        movies.append(media.Movie(row[0],row[1],row[2],row[3]))
finally:
    f.close()

# creating the web page
fresh_tomatoes.open_movies_page(movies)
