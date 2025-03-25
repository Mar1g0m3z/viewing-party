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

def get_watched_avg_rating(user_data):
    total = 0
    count = 0
    if not user_data["watched"]:
        return 0
    for data in user_data["watched"]:
        total += data["rating"]
        count += 1
    average = total / count

    return average


def get_most_watched_genre(user_data):
    genres = []
    if not user_data["watched"]:
        return None
    for data in user_data["watched"]:
        genres.append(data["genre"])
    top_genre = ""
    top_count = 0
    for genre in genres:
        genre_count = genres.count(genre)
        if (genre_count > top_count):
            top_count = genre_count
            top_genre = genre
    return top_genre


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    if not user_data["watched"]:
        return []
    friends_watched = []
    user_unique_movies = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched.append(movie["title"])
    for data in user_data["watched"]:
        if data["title"] not in friends_watched:
            user_unique_movies.append(data)
    return user_unique_movies


def get_friends_unique_watched(user_data):
    user_watched = user_data["watched"]
    friends_unique_movie = []
    for friend in user_data["friends"]:
        for data in friend["watched"]:
            if data not in user_watched and data not in friends_unique_movie:
                friends_unique_movie.append(data)
    return friends_unique_movie


# -----------------------------------------
# ------------- WAVE 4 --------------------

# -----------------------------------------
def get_available_recs(user_data):
    # subscriptions - what user has
    # host - where the movie is hosted
    #  list of movies that friends have watch and user has not
    # movies must be in host the user has
    recommendations = []
    print(user_data["subscriptions"])
    friends_unique = get_friends_unique_watched(user_data)
    for data in friends_unique:
        if data["host"] in user_data["subscriptions"]:
            recommendations.append(data)

    return recommendations

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------


def get_new_rec_by_genre(user_data):
    # find top user genre
    # get list of friends unique movie
    # add to empty genre rec only if genre of the movies is equal to user favorite
    # return list
    user_genre = get_most_watched_genre(user_data)
    friends_unique = get_friends_unique_watched(user_data)
    genre_reqs = []
    for data in friends_unique:
        if data["genre"] == user_genre:
            genre_reqs.append(data)
    return genre_reqs


def get_rec_from_favorites(user_data):
    # user data has "favorites"
    # put movies in list only if in user favorites
    # AND NOT in friend's watched
    favorites_recs = []
    user_unique = get_unique_watched(user_data)
    for data in user_unique:
        if data in user_data["favorites"]:
            favorites_recs.append(data)
    return favorites_recs
