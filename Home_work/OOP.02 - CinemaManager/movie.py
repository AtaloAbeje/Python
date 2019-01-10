class Movie:
    def __init__(self, MoviesName, MovieLength):
        self.MoviesName = MoviesName
        self.MovieLength = MovieLength

    def get_info(self): # return only string
        return "Movie Name: " + self.MoviesName + "Length: " + str(self.MovieLength) # convert to string the num of length
