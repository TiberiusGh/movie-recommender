def pearson_alg(person_a, person_b):
    movies = shared_movies(person_a, person_b)

    average_a = average_rating(person_a, movies)
    average_b = average_rating(person_b, movies)

    # Calculate deviation from the average rating
    # Calculate r
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


def average_rating(person, shared_movies):
    total = 0

    for movie_id in shared_movies:
        total += person[movie_id]

    average_rating = total / len(shared_movies)
    return average_rating