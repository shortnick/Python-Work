from movieClassDB import Movie
from userMovie import User
import json

#user = User("Bob")

"""
my_movie = Movie("The Matrix", "Wachowskis", "Science Fiction", True)
user.movies.append(my_movie)

my_movie = Movie("Fight Club", "Dude", "Thriller", True)
user.movies.append(my_movie)
"""
#print(user.watched_movies())
#user.delete_movie("The Matrix")

#user.save_to_file()

#user = User.load_from_file("Bob.txt")
#with open("Bob.txt",'w') as f:
#   json.dump(user.json(),f)

with open("Bob.txt",'r') as f:
    json_data = json.load(f)
    user = User.load_from_json(json_data)

print(user.json())
