from math import sqrt

def pearson_alg(person_a, person_b):
    movies = shared_movies(person_a, person_b)
    if len(movies) == 0:
        return 0

    average_a = average_rating(person_a, movies)
    average_b = average_rating(person_b, movies)

    numerator = 0 # How much they agree
    spread_a = 0
    spread_b = 0

    for movie_id in movies:
        deviation_person_a = person_a[movie_id] - average_a
        deviation_person_b = person_b[movie_id] - average_b

        numerator += deviation_person_a * deviation_person_b

        # Stop the deviations from cancelling out
        spread_a += deviation_person_a ** 2 
        spread_b += deviation_person_b ** 2

    denominator = sqrt(spread_a * spread_b) # Maximum possible agreement

    if denominator == 0:
        return 0

    r = numerator / denominator
    return r



def shared_movies(person_a, person_b):
    shared_movies = []

    for movie_id in person_a:
        if movie_id in person_b:
            shared_movies.append(movie_id)

    return shared_movies


def average_rating(person, shared_movies):
    total = 0

    for movie_id in shared_movies:
        total += person[movie_id]

    average_rating = total / len(shared_movies)
    return average_rating