import os
import json
from userMovie import *
from movieClassDB import Movie

def menu():
    name = input("What is your name? (first last)")
    filename = "{}.txt".format(name)

    if file_exists(filename):
        with open(filename, 'r') as f:
            json_data = json.load(f)
            user = User.load_from_json(json_data)
    else:
        user = User(name)

    userinput = input("Enter 'a' to add movie, 's' to see list of movies,"
          "'w' to tag movie as watched, 'd' to delete a movie, 'l' to list watched movies,"
          "or 'q' to save and quit")

    while userinput != 'q':
        if userinput == 'a':
            movie_input= input(" Enter: movie name, director, genre")
            movie_input = movie_input.split(",")
            print(movie_input)
            watched = input("Have you watched this movie? (y/n)")
            if watched == "y":
                watched = True
                movie_input.append(watched)
            else:
                watched = False
                movie_input.append(watched)
            user.add_movie(*movie_input)

        elif userinput == 's':
            for m in user.movies:
                m.show_movie()

        elif userinput == 'w':
            user_input = input("What film have you watched?")
            for m in user.movies:
                if m.name == user_input:
                    m.watched = True
                    print("Changed.")

        elif userinput == 'd':
            user_input = input("Which movie do you want to delete?")
            for m in user.movies:
                if m.name == user_input:
                    user.delete_movie(user_input)
                    print("Deleted.")


        elif userinput == 'l':
            print(user.watched_movies())

        elif userinput == 'q':
            with open(filename, 'w') as f:
                json.dump(user.json(),f)
                print("Exiting.")

        else:
            menu()

        userinput = input("Enter 'a' to add movie, 's' to see list of movies,"
          "'w' to tag movie as watched, 'd' to delete a movie, 'l' to list watched movies,"
          "or 'q' to save and quit")

def file_exists(testing):
    return os.path.isfile(testing)

menu()
