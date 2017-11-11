import webbrowser

# This file holds the classes to make movie and TV show objects


# Abstract Parent Class
class Video():
    """ This abstract class provides a way to store video
        instance information found in entertainment_center.py """
    # Constructor gathers title, storyline, poster image, and trailer
    def __init__(self, title, storyline, poster_image_url,
                 trailer_youtube_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    # Open a browser window displaying the video's poster
    def show_poster(self):
        webbrowser.open(self.poster_image_url)

    # Open a browser window displaying the video's youtube trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


# Movie child class inherits from Video parent class
class Movie(Video):
    """ This class creates a movie object by storing movie
        instance information found in entertainment_center.py """
    # Constructor also gathers duration
    def __init__(self, title, storyline, poster_image_url,
                 trailer_youtube_url, duration):
        # Inherited instance variables
        Video.__init__(self, title, storyline, poster_image_url,
                       trailer_youtube_url)
        # Local instance variable
        self.duration = duration

    # print the duration of the movie
    def show_duration(self):
        print self.duration


# TvShow child class inherits from Video parent class
class TvShow(Video):
    """ This class creates a TV show object by storing TV
        instance information found in entertainment_center.py """
    # Constructor also gathers number of seasons and episodes
    def __init__(self, title, storyline, poster_image_url,
                 trailer_youtube_url, num_seasons, num_episodes):
        # Inherited instance variables
        Video.__init__(self, title, storyline, poster_image_url,
                       trailer_youtube_url)
        # Local instance variables
        self.num_seasons = num_seasons
        self.num_episodes = num_episodes

    # print the number of seasons for the TV show
    def show_seasons(self):
        print self.num_seasons

    # print the number of episodes for the TV show
    def show_episodes(self):
        print self.num_episodes
