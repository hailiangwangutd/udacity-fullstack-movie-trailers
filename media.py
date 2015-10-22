import webbrowser
import fresh_tomatoes
import csv


class Movie():
    """ This class provides a way to store movie related information"""

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, title, movie_actor, poster_image_url, trailer_youtube_url):
        self.title = title
        self.movie_actor = movie_actor
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url


def get_movies(filename):
    """ pulls movie data from csv and returns a list a Movie objects """
    movies = []
    with open('data.csv', 'r') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:

            movies.append(Movie(row[0], row[1], row[2], row[3]))
    return movies


def main():
    """ main subroutine """
    movies = get_movies('data.csv')
    fresh_tomatoes.open_movies_page(movies)

if __name__ == '__main__':
    main()
