import fresh_tomatoes #importing fresh_tomatoes file
import media  #importing media file 

see_me = media.Movie("now u see me","its one of my favourite films",
                   "https://images-na.ssl-images-amazon.com/images/M/MV5BMTY0NDY3MDMxN15BMl5BanBnXkFtZTcwOTM5NzMzOQ@@._V1_UY1200_CR70,0,630,1200_AL_.jpg", # NOQA
                   "https://www.youtube.com/watch?v=KzJNYYkkhzc")

pirates = media.Movie("pirates of the caribbean" , "its a good film & recommended to you",
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BMjAyNDM4MTc2N15BMl5BanBnXkFtZTYwNDk0Mjc3._V1_UY1200_CR90,0,630,1200_AL_.jpg", # NOQA
                      "https://www.youtube.com/watch?v=a5V5C8mEVzY")

toy_story = media.Movie("Toy story","a story of toy ",
                        "https://a.dilcdn.com/bl/wp-content/uploads/sites/8/2013/02/toy_story_wallpaper_by_artifypics-d5gss19.jpg", # NOQA
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar","avatar is an animation movie",
                     "http://t0.gstatic.com/images?q=tbn:ANd9GcQCfmvrE4fMo2cd8esc7mDZPtFSJThAujddMPkRtti1_ij6u-jp", # NOQA
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

death_note = media.Movie("death note", "it's a wonderfull movie really",
                         "http://blog.honeyfeed.fm/wp-content/uploads/2015/10/death-note-live-action.jpg",
                         "https://www.youtube.com/watch?v=zS9UW2xjdqE")

shawshank = media.Movie("shawshank redemption","no one can deny that it's an amazing old film",
                        "http://img.goldposter.com/2015/04/The-Shawshank-Redemption_poster_goldposter_com_33.jpg@0o_0l_800w_80q.jpg", # NOQA
                        "https://www.youtube.com/watch?v=6hB3S9bIaco")

'''
in the above we make 6 objects from the class Movie which created in media file
each single object represent Movie class
as ex: avatar is an object which take his title,story_line ,poster & trailer as
       arguments exactly as class Movie .
and so on we make the same thing to all of 6 objects.       
'''



movies = [see_me , pirates , toy_story , avatar , death_note , shawshank] #list of movies instances

fresh_tomatoes.open_movies_page(movies)
''' invoke open_movies_page() function which declared in fresh_tomatoes file
this function takes one argument, which is a list of movies and creates
an HTML file which visualizes all of your favorite movies. '''



