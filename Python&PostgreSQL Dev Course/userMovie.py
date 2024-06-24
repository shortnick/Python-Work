from movieClassDB import Movie
class User:
    def __init__(self, name):
        self.name = name
        self.movies = []

    def __repr__(self):
        return "<User {}>".format(self.name)

    def add_movie(self, name, director, genre, watched):
        self.movies.append(Movie(name, director, genre, watched))

    def show_movie(self):
        print("Movie: {}, Director: {}, Genre: {}, Watched: {}".format(*self))

    def delete_movie(self, name):
        self.movies = list(filter(lambda movie: movie.name != name, self.movies))

    def watched_movies(self):
        watched = list(filter(lambda x: x.watched, self.movies))
        output = []
        for x in watched:
            output.append(x.show_movie())
            output = list(filter(lambda x: None, output))
        return output

    def set_watched(self, name):
        for movie in self.movies:
            if movie.name == name:
                movie.watched = True

    def json(self):
        return {
            'name':self.name,
            'movies': [
                x.json() for x in self.movies
            ]
        }

    def save_to_file(self):
        with open("{}.txt".format(self.name), 'w') as f:
            f.write(self.name + ", \n")
            for x in self.movies:
                f.write("{}, {}, {}, {},\n".format(x.name, x.director, x.genre, str(x.watched)))

    def save_to_json(self):
        with open("{}.json".format(self.name), 'w') as f:
            f.write(self.name + ", \n")

    @classmethod
    def load_from_csv(cls, filename):
        with open(filename, 'r') as myFile:
            user_data = myFile.readlines()
            username = user_data[0]
            movies = []
            for m in user_data[1:]:
                incoming = m.split(",")
                movies.append(Movie(incoming[0], incoming[1], incoming[2], incoming[3] == "True"))

            user = User(username)
            user.movies = movies
            return user

    @classmethod
    def load_from_json(cls, json_data):
        user = User(json_data['name'])
        movies = []
        for m in json_data['movies']:
           movies.append((Movie.from_json(m)))
        user.movies = movies
        return user
