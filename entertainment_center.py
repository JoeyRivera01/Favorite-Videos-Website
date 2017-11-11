import media
import fresh_tomatoes

# Main file used to create video objects and call fresh_tomatoes function

# Instances of movies
reservoir_dogs = media.Movie(
    "Reservoir Dogs",
    "Five strangers team up for the perfect crime.",
    "https://www.movieposter.com/posters/archive/main/12/A70-6021",
    "https://www.youtube.com/watch?v=vayksn4Y93A",
    "1h 39m")

matrix = media.Movie(
    "Matrix",
    'In a dystopian future, reality perceived by most huamns is actually '
    'a simulated reality called "the Matrix".',
    "https://images-na.ssl-images-amazon.com/images/I/51k1epcewKL.jpg",
    "https://www.youtube.com/watch?v=vKQi3bBA1y8",
    "2h 30m")

eternal_sunshine = media.Movie(
    "Eternal Sunshine of the Spotless Mind",
    "After a painful breakup, Clementine undergoes a procedure to erase "
    "memories of her former boyfriend, Joel.",
    "http://horrornews.net/wp-content/uploads/2015/05/"
    "Eternal-Sunshine-poster.jpg",
    "https://www.youtube.com/watch?v=0zFywiAh7N0",
    "1h 48m")

her = media.Movie(
    "Her",
    "Theodore becomes fascinated with a new operating system which "
    "reportedly develops into an intuitive, and unique entity.",
    "https://20ui41tp7v127j03rcnp97oh-wpengine.netdna-ssl.com/wp-content/"
    "uploads/2016/02/cooper_her.jpg",
    "https://www.youtube.com/watch?v=WzV6mXIOVl4",
    "2h 6m")

cabin_in_the_woods = media.Movie(
    "Cabin in the Woods",
    "When five college friends arrive at a remote forest cabin for vacation, "
    "they do not expect the horrors that await them.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BNTUxNzYyMjg2N15BMl5"
    "BanBnXkFtZTcwMTExNzExNw@@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
    "https://www.youtube.com/watch?v=rXMfTm2Hbig",
    "1h 35m")

get_out = media.Movie(
    "Get Out",
    "Chris meets his girlfriend's White parents and discovers"
    "something disturbing.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BNTE"
    "2Nzg1NjkzNV5BMl5BanBnX"
    "kFtZTgwOTgyODMyMTI@._V1_UY1200_CR64,0,630,1200_AL_.jpg",
    "https://www.youtube.com/watch?v=A2JbO9lnVLE",
    "1h 44m")

# Instances of TV shows
breaking_bad = media.TvShow(
    "Breaking Bad",
    "A once loyal father and chemistry teacher, Walter White, "
    "turns to a life of crime due to developing stage 3 terminal lung cancer.",
    "https://i.pinimg.com/736x/0d/11/2e/0d112e94f0d614e9740ec59f29153639"
    "--tv-show-breaking-bad-poster.jpg",
    "https://www.youtube.com/watch?v=HhesaQXLuRY",
    "5",
    "62")

the_wire = media.TvShow(
    "The Wire",
    "Set in Baltimore, this show centers around the city's inner-city"
    "drug scene.",
    "http://www.michaeldvd.com.au/CoverArtUnverified/16256.jpg",
    "https://www.youtube.com/watch?v=uDcQbk78CSw",
    "5",
    "60")

fire_fly = media.TvShow(
    "Firefly",
    "Set in the distant future, Malcolm Reynolds is the captain of the ship "
    "Serenity, a Firefly class transport. "
    "They do what they have to do to survive.",
    "http://cdn.collider.com/wp-content/uploads/firefly-dvd-box-cover-01.jpg",
    "https://www.youtube.com/watch?v=mG9bSBGLtMc",
    "1",
    "14")

star_trek_ng = media.TvShow(
    "Star Trek: The Next Generation",
    "Jean-luc Picard is the captain of the U.S.S. Enterprise "
    "(NCC-1701-d) in the 24th century. This show follows his crew as they "
    "explore space, the final frontier.",
    "https://fanart.tv/fanart/tv/71470/tvposter/star-trek-the-next"
    "-generation-5212cca6"
    "6f1d9.jpg",
    "https://www.youtube.com/watch?v=jtmsI07AMsE",
    "7",
    "178")

game_of_thrones = media.TvShow(
    "Game of Thrones",
    "Winter is coming.",
    "https://i.pinimg.com/736x/ba/c1/a1/bac1a13f"
    "5f115ba51eb02083770aa522.jpg",
    "https://www.youtube.com/watch?v=522l0YE9hRQ",
    "7",
    "67")

walking_dead = media.TvShow(
    "The Walking Dead",
    "Deputy Rick Grimes wakes from a coma discovering a world "
    "overrun by zombies. How will he survive?",
    "http://cdn.collider.com/wp-content/uploads/"
    "walking_dead_one_sheet_poster.jpg",
    "https://www.youtube.com/watch?v=R1v0uFms68U",
    "7",
    "99")

# List of movies
movies = [reservoir_dogs, matrix, eternal_sunshine,
          her, cabin_in_the_woods, get_out]
# List of TV shows
tv_shows = [breaking_bad, the_wire, fire_fly,
            star_trek_ng, game_of_thrones, walking_dead]

""" Comment out TV function call and uncomment
    movie function call to the see movie page """

# Overwrites HTML and opens a webpage displaying movies
# fresh_tomatoes.open_movies_page(movies)

# Overwrites HTML and opens a webpage displaying TV shows
fresh_tomatoes.open_tv_page(tv_shows)
