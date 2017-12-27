import webbrowser

class Movie():
   '''This class is a template to store details about a movie'''

   def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):

       self.title = movie_title
       self.storyline = movie_storyline
       self.poster_image_url = poster_image
       self.trailer_youtube_url = trailer_youtube

   # following is a method to show trailer given a url
   def show_trailer(self):
       webbrowser.open(self.trailer_youtube_url)
       
