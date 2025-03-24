# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):

    if not title or not genre or not rating:
        return None
    new_movie = {"title": title, "genre": genre, "rating": rating}
    return new_movie


def add_to_watched(user_data, movie):
    # print("AAAAAAAAAAA")

    user_data["watched"].append(movie)

    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, movie):
    for movies in user_data["watchlist"]:
        if movies["title"] == movie:
            user_data["watched"].append(movies)
            user_data["watchlist"].remove(movies)

    return user_data


user_data = {"watched": [], "watchlist": [{
    "title": "MOVIE_TITLE_1",
    "genre": "GENRE_1",
    "rating": "RATING_1"
}]}
movie = {
    "title": "MOVIE_TITLE_1",
    "genre": "GENRE_1",
    "rating": "RATING_1"
}
print(watch_movie(user_data, movie))

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
