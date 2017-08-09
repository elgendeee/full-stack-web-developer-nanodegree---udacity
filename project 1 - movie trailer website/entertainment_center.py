import media #file where Movie class is created in.
import fresh_tomatoes #to help generate a website that displays these movies.

#Making instancies of our class Movie.And passing arguments through constructor.

whiplash = media.Movie("Whiplash" ,
                       "A film depicting the relationship between an "
                       "ambitious jazz student and an abusive instructor" ,
                       "https://upload.wikimedia.org/wikipedia/en/thumb/0/01/Whiplash_poster.jpg/220px-Whiplash_poster.jpg" ,  # NOQA
                       "https://www.youtube.com/watch?v=7d_jQycdQGo")

the_dark_knight_rises = media.Movie("The dark knight rises" ,
                                    "A story of a batman and joker" ,
                                    "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg" ,  # NOQA
                                    "https://www.youtube.com/watch?v=EXeTwQWrcwY")

saving_private_ryan = media.Movie("Saving private ryan" ,
                                  "Captain John Miller (Tom Hanks) takes "
                                  "his men behind enemy lines to find Private "
                                  "James Ryan, whose three brothers have been "
                                  "killed in combat" ,
                                  "http://t2.gstatic.com/images?q=tbn:ANd9GcR0lDhR_dXAKTm9wysp3nWu6kP0V5skJBVbCNC_Q8urAWcr4iF_" ,  # NOQA
                                  "https://www.youtube.com/watch?v=h5p5j_K0CsY")

fight_club = media.Movie("Fight club" ,
                         "A ticking-time-bomb insomniac and a slippery soap "
                         "salesman channel primal male aggression into "
                         "a shocking new form of therapy. " ,
                         "https://upload.wikimedia.org/wikipedia/en/thumb/f/fc/Fight_Club_poster.jpg/220px-Fight_Club_poster.jpg" ,  # NOQA
                         "https://www.youtube.com/watch?v=SUXWAEX2jlg")

the_green_mile = media.Movie("The green mile" ,
                             "Paul Edgecomb (Tom Hanks) walked the mile with "
                             "a variety of cons. He had never encountered "
                             "someone like John Coffey (Michael Clarke Duncan), "
                             "a massive black man convicted of brutally killing "
                             "a pair of young sisters." ,
                             "http://t3.gstatic.com/images?q=tbn:ANd9GcRzAo286udsv_uTTpuBmSc3_h-nlUaWHYcUYG6VMAhhPcSDLJF7" ,  # NOQA
                             "https://www.youtube.com/watch?v=Ki4haFrqSrw")

the_prestige = media.Movie("The prestige" ,
                           "Robert Angier and Alfred Borden, rival stage "
                           "magicians in London at the end of the 19th "
                           "century. Obsessed with creating the best stage "
                           "illusion, they engage in competitive one-upmanship "
                           "with tragic results." ,
                           "https://upload.wikimedia.org/wikipedia/en/d/d2/Prestige_poster.jpg" ,  # NOQA
                           "https://www.youtube.com/watch?v=o4gHCmTQDVI")

mr_nobody = media.Movie("Mr Nobody" ,
                        "A boy stands on a station platform as a train is "
                        "about to leave. Should he go with his mother or stay "
                        "with his father? Infinite possibilities arise" ,
                        "https://upload.wikimedia.org/wikipedia/en/3/32/Mr._Nobody_%28film_poster%29.jpg" ,  # NOQA
                        "https://www.youtube.com/watch?v=mpi0qsp3v_w")

night_crawler = media.Movie("Night crawler" ,
                            "Lou Bloom, a stringer who records violent events "
                            "late at night in Los Angeles, and sells the "
                            "footage to a local television news station" ,
                            "https://upload.wikimedia.org/wikipedia/en/d/d4/Nightcrawlerfilm.jpg" , # NOQA
                            "https://www.youtube.com/watch?v=X8kYDQan8bw")

hacksaw_ridge = media.Movie("Hacksaw Ridge" ,
                            "Hacksaw Ridge is a 2016 biographical war drama "
                            "film about the World War II experiences of "
                            "Desmond Doss, an American pacificist combat "
                            "medic who was a Seventh-day Adventist Christian, "
                            "refusing to carry or use a firearm or weapons of "
                            "any kind." ,
                            "https://upload.wikimedia.org/wikipedia/en/8/8a/Hacksaw_Ridge_poster.png" , # NOQA
                            "https://www.youtube.com/watch?v=s2-1hz1juBI")

#putting movies in a list to use it in open_movies_page() function.
movies = [whiplash ,
          the_dark_knight_rises ,
          saving_private_ryan ,
          fight_club ,
          the_green_mile ,
          the_prestige ,
          mr_nobody ,
          night_crawler ,
          hacksaw_ridge]

fresh_tomatoes.open_movies_page(movies)
