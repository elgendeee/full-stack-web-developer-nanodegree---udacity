import webbrowser

class Movie() :

    """this is a class to show movies trailers and their information."""

    def __init__(self , movie_title ,
                 movie_storyline ,
                 poster_image ,
                 trailer_youtube) :

        """this is a fucnction to initialize the variables of the instance."""
        
	#initializing arguments to instance variables.
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

     #Functionality of openning the trailer url.   
    def show_trailer(self) :
	    
	    """this is a fuction to open youtube links of the movie."""
            webbrowser.open(self.trailer_youtube_url)
