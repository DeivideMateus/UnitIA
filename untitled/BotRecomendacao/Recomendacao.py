import pandas as pd

idx = pd.IndexSlice
links = pd.read_csv("links.csv", index_col=['movieId'])
movies = pd.read_csv("movies.csv", sep=",", index_col=['movieId'])
ratings = pd.read_csv("ratings.csv", index_col=['userId', 'movieId'])
tags = pd.read_csv("tags.csv", index_col=['userId', 'movieId'])


def get_movies_by_user(id_user, rating_cut=0, list_=False):
    return_dict = {}
    dict_ = ratings.loc[idx[id_user, :], 'rating'].T.to_dict()

    for d in dict_:
        if rating_cut != 0:
            if dict_[d] >= rating_cut:
                return_dict[d[1]] = dict_[d]
        else:
            return_dict[d[1]] = dict_[d]

    if list_:
        return list(return_dict.keys())

    return return_dict


def get_users_by_movie(id_movie, rating_cut=0, list_=False):
    return_dict = {}
    dict_ = ratings.loc[idx[:, id_movie], 'rating'].T.to_dict()
    for d in dict_:
        if rating_cut != 0:
            if dict_[d] >= rating_cut:
                return_dict[d[0]] = dict_[d]
        else:
            return_dict[d[0]] = dict_[d]

    if list_:
        return list(return_dict.keys())

    return return_dict


def get_rating_by_user_movie(id_user, id_movie):
    rating = 0.0;

    try:
        rating = ratings.loc[idx[id_user, id_movie], 'rating']
    except KeyError as e:
        rating = 0.0

    return rating


def get_all_users():
    return list(set([x[0] for x in ratings.index.values]))


def get_movie_title(id_movie):
    info = movies.loc[idx[id_movie], :]
    return info['title']


def get_imdb_id(id_movie):
    imdbid = int(links.loc[idx[id_movie], 'imdbId'])

    imdbid = "tt%.7d" % imdbid

    return imdbid


all_users = get_all_users()

movies_user_true = {}
movies_user_false = {}

for user in all_users:
    movies_user_true[user] = get_movies_by_user(user, list_=True)
    movies_user_false[user] = get_movies_by_user(user, list_=False)


def recomendacao(user):
    selected_user = user

    my_movies = get_movies_by_user(selected_user, rating_cut=4, list_=True)

    all_users = []

    for movie in my_movies:
        all_users = all_users + get_users_by_movie(movie, rating_cut=5, list_=True)

        all_users = list(set(all_users))

        all_movies = []

    for user in all_users:
        movies_ = get_movies_by_user(user, rating_cut=5, list_=True)
        all_movies = all_movies + movies_

    all_movies = list(set(all_movies) - set(my_movies))

    return all_movies


def getRecomendacao(user):
    filmes = recomendacao(user)
    count = 1
    msg = ""
    for movie in filmes[:10]:
        msg = msg + "\n" + str(count) + " " + get_movie_title(movie)
        count += 1

    return msg


