import media
import fresh_tomatoes

# Initializing different instances of Movie class

scary_movie = media.Movie("scary movie",
                          "http://hdpopcorns.co/wp-content/uploads/2016/03/Cover_image-Scary-Movie-2000.jpg",  # NOQA
                          "The film is a parody of the horror,\
                          slasher, and mystery film genres.",
                          "https://www.youtube.com/watch?v=_dktIVAfjzY")
dunkirk = media.Movie("Dunkirk",
                      "http://hdpopcorns.co/wp-content/uploads/2017/12/Cover_image-Dunkirk-2017-720p-free-movie-download.jpg",  # NOQA
                      "Evacuation of Allied soldiers from Belgium, \
                       who were cut off and surrounded \
                       in World War II.",
                      "https://www.youtube.com/watch?v=F-eMt3SrfFU")
deadpool_2 = media.Movie(
                         "DeadPool 2",
                         "http://hdpopcorns.co/wp-content/uploads/2018/08/Cover_image-Deadpool-2-2018-720p-free-movie-download.jpg",  # NOQA
                         "Deadpool (Ryan Reynolds) must protect Russel (Julian Dennison)\
                          must assemble a team \
                          of mutants and protect Russel from \
                          Cable (Josh Brolin), \
                          a no-nonsense, dangerous cyborg from the future and \
                          Deadpool must learn the most important lesson of \
                          all, to be part of a family again",
                         "https://www.youtube.com/watch?v=D86RtevtfrA")
avengers_infi = media.Movie("Avengers: Infinity wars",
                            "http://hdpopcorns.co/wp-content/uploads/2018/08/Cover_image-Avengers-Infinity-War-2018-720p-free-movie-download.jpg",  # NOQA
                            "As the Avengers and their allies have continued to protect the world from \
                            threats too large for any one hero to handle, \
                            a new danger has emerged from the cosmic \
                            shadows: Thanos.",
                            "https://www.youtube.com/watch?v=6ZfuNTqbHE8")

# Making a list of different instances of class Movie
movies = [scary_movie, dunkirk, deadpool_2, avengers_infi]

# Provide the list of movies to open_movies_page function
fresh_tomatoes.open_movies_page(movies)
