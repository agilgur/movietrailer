import webbrowser

class Movie():
	'''This class creates Movie objects (instances) defined in myMovies.py'''
	def __init__(self, movie_title, movie_storyline, 
				 poster_image, trailer_youtube):
		'''Initializing data associated with instance of class Movie''' 
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)




        
