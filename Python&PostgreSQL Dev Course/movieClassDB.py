
class Movie:
    def __init__(self, name, director, genre, watched):
        self.name = name
        self.director = director
        self.genre = genre
        self.watched = watched

    def __repr__(self):
        return "<Movie: {}>".format(self.name)

    def show_movie(self):
        print("Movie: {}, Director: {}, Genre: {}, Watched: {}".format(
            self.name, self.director, self.genre, self.watched))

    def json(self):
        return {
            "name":self.name,
            "director": self.director,
            "genre": self.genre,
            "watched": self.watched
        }
    def from_json(m):
        #takes json of Movie class object, returns actual Movie class object
        return Movie(**m)
