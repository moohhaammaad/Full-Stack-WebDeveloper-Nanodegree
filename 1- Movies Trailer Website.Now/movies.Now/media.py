import webbrowser   

class Movie():
    #initialization function which take the title,story,poster & trailer as an arguments to the movie
    def __init__(self,movie_title,story_line,
                 poster_image,youtube_trailer):
        self.title=movie_title
        self.story=story_line
        self.poster_image_url=poster_image
        self.trailer_youtube_url=youtube_trailer


    def  show_trailer(self):
    # this function open the url in the web browser
        webbrowser.open(self.trailer_youtube_url)




