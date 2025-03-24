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


# use_data = {"watched": []}
# movie = {
#     "title": "MOVIE_TITLE_1",
#     "genre": "GENRE_1",
#     "rating": "RATING_1"
# }
# print(add_to_watched(use_data, movie))
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
