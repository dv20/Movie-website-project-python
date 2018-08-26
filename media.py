import webbrowser


class Movie():
    '''This class stores data of different movies'''
    def __init__(self, movie_title, movie_poster, movie_info, movie_trailer):
        # initializing variables using constructor __init__
        # It takes movie title
        self.title = movie_title
        # It takes image url of movie
        self.poster_image_url = movie_poster
        # It takes youtube trailer url
        self.trailer_youtube_url = movie_trailer
        # Synopsis of movie
        # self.movie_info = movie_info

    # This function is used to play trailer
    def show_trailer(self):
        # In built function which allows us to open web browser
        webbrowser.open(self.trailer_youtube_url)