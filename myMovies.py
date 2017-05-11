import fresh_tomatoes
import media

# Instances of the class Movie created in media.py are defined here. 
# Each contains the movie title, storyline, poster URL and a YouTube link.


frida = media.Movie("Frida", 
                    "A biography of artist Frida Kahlo, who channeled the pain" 
                    "of a crippling injury and her tempestuous marriage into her work.",
                    "https://upload.wikimedia.org/wikipedia/en/2/26/Fridaposter.jpg",
                    "https://www.youtube.com/watch?v=uOUzQYqba4Y")

forrest_gump = media.Movie("Forrest Gump", 
                           "Forrest Gump, while not intelligent, has accidentally been present"
                           "at many historic moments, but his true love, Jenny Curran, eludes him.",
                           "https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg", 
                           "https://www.youtube.com/watch?v=uPIEn0M8su0")

shawshank_redemption = media.Movie("The Shawhank Redemption",
                                   "Two imprisoned men bond over a number of years, finding solace"
                                   "and eventual redemption through acts of common decency.",
                                   "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
                                   "https://www.youtube.com/watch?v=6hB3S9bIaco")

pulp_fiction = media.Movie("Pulp Fiction",
                           "The film connects the intersecting storylines of Los Angeles mobsters"
                           "fringe players, small-time criminals, and a mysterious briefcase.",
                           "https://upload.wikimedia.org/wikipedia/en/3/3b/Pulp_Fiction_%281994%29_poster.jpg",
                           "https://www.youtube.com/watch?v=wZBfmBvvotE")

memento = media.Movie("Memento",
                      "A man juggles searching for his wife's murderer and keeping his"
                      "short-term memory loss from being an obstacle.", 
                      "https://upload.wikimedia.org/wikipedia/en/c/c7/Memento_poster.jpg",
                      "https://www.youtube.com/watch?v=0vS0E9bBSL0")

eye_wide_shut = media.Movie("Eyes Wide Shut",
                            "A New York City doctor, who is married to an art curator,"
                            "pushes himself on a harrowing and dangerous night-long"
                            "odyssey of sexual and moral discovery after his wife admits"
                            "that she once almost cheated on him.",
                            "https://upload.wikimedia.org/wikipedia/en/8/87/Eyes_Wide_Shut_poster.jpg",
                            "https://www.youtube.com/watch?v=YEfyfcEdW4Y")

pianist= media.Movie("The Pianist",
                     "A Polish Jewish musician struggles to survive the" 
                     "destruction of the Warsaw ghetto of World War II.",
                     "https://upload.wikimedia.org/wikipedia/en/a/a6/The_Pianist_movie.jpg",
                     "https://www.youtube.com/watch?v=u_jE7-6Uv7E")

volver = media.Movie("Volver",
                     "After her death, a mother returns to her home town in" 
                     "order to fix the situations she couldn't resolve during her life.",
                     "https://upload.wikimedia.org/wikipedia/en/2/2b/Volver_Poster.jpg",
                     "https://www.youtube.com/watch?v=ABSvppyQGdE",)


eternal_sunshine = media.Movie("Eternal Sunshine of The Spotless Mind",
                               "When their relationship turns sour, a couple undergoes" 
                               "a procedure to have each other erased from their memories."
                               "But it is only through the process of loss that they"
                               "discover what they had to begin with.",
                               "https://upload.wikimedia.org/wikipedia/en/6/62/Eternal_sunshine_of_the_spotless_mind_ver3.jpg",
                               "https://www.youtube.com/watch?v=yE-f1alkq9I")

secret_life_of_pets = media.Movie("Secret Life of Pets",
                                  "The quiet life of a terrier named Max is upended when" 
                                  "his owner takes in Duke, a stray whom Max instantly dislikes.",
                                  "https://upload.wikimedia.org/wikipedia/en/6/64/The_Secret_Life_of_Pets_poster.jpg",
                                  "https://www.youtube.com/watch?v=eWI_Jsw9qUs")



# A list of movies created previously
movies= [frida, forrest_gump, shawshank_redemption, pulp_fiction,
         memento, eye_wide_shut, pianist, volver, eternal_sunshine, 
         secret_life_of_pets]



# This function uses a list of movie instances as input to generate an 
# HTML file and open it in the browser.
fresh_tomatoes.open_movies_page(movies)




