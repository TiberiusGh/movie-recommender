def pearson_alg(person_a, person_b):
    movies = shared_movies(person_a, person_b)

    total_person_a = 0
    total_person_b = 0

    for movie_id in shared_movies:
        total_person_a += person_a[movie_id]
        total_person_b += person_b[movie_id]

    nr_shared_movies = len(shared_movies)

    average_person_a = total_person_a / nr_shared_movies
    average_person_b = total_person_b / nr_shared_movies

    deviation_person_a = person_a[movie_id] - average_person_a
    deviation_person_b = person_b[movie_id] - average_person_b

    return 


def shared_movies(person_a, person_b):
    shared_movies = []

    for movie_id in person_a:
        if movie_id in person_b:
            shared_movies.append(movie_id)

    if len(shared_movies) == 0:
        return 0

    return shared_movies
