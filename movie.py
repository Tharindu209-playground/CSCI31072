class Movie:
    def __init__(self, title, genre, rating):
        self.title = title
        self.genre = genre
        self.rating = rating

class MovieDatabase:
    def __init__(self):
        self.movies = []
        self.genres = set()

    def add_movie(self, movie):
        self.movies.append(movie)
        self.genres.add(movie.genre)
        print(f"Added movie '{movie.title}' to the database.")

    def search_by_genre(self, genre):
        return [movie for movie in self.movies if movie.genre == genre]

    def display_sorted_movies(self):
        sorted_movies = sorted(self.movies, key=lambda m: m.rating, reverse=True)
        for movie in sorted_movies:
            print(f"{movie.title} - Rating: {movie.rating}")

db = MovieDatabase()
db.add_movie(Movie("Inception", "Sci-Fi", 8.8))
db.add_movie(Movie("The Matrix", "Sci-Fi", 8.7))
db.add_movie(Movie("Good Will Hunting", "drama", 8.3))
db.add_movie(Movie("Ray", "Musical", 7.7))
db.display_sorted_movies()
