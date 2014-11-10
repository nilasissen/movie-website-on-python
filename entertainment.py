import fresh_tomatoes
import media


toy_story = media.Movie("toy story","A story of a boy and his toys that come to life",
                        "http://goo.gl/gMbBMx","http://www.youtube.com/watch?v=KYz2wyBy3kc")



avatar = media.Movie("AVATAR"," A man in a alian planet","http://goo.gl/yOXosa",
                     "http://www.youtube.com/watch?v=_Tkc5pQp_JE")

hunger_game = media.Movie("hunger game"," even i am not sure what it is","http://goo.gl/U7R1mA",
                     "http://www.youtube.com/watch?v=FovFG3N_RSU")
movies = [toy_story,avatar,hunger_game]
fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.valid_ratings)
