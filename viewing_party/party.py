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
    print(user_data)
    for movies in user_data["watchlist"]:
        for keys, values in movies.items():
            print(values)
            if movie == values:
                watched_movie = user_data["watchlist"][0].pop(movie)
                user_data["watched"] = watched_movie
            # print(len(user_data["watchlist"]))
        # print(user_data["watchlist"])
    # user_data["watched"].append(movie)
    print(len(user_data["watched"]))

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
