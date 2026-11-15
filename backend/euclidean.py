def euclidean_alg(person_a, person_b):
    total = 0
    shared_movies = 0

    for movie_id in person_a:
        if movie_id in person_b:
            difference = person_a[movie_id] - person_b[movie_id]

            total += difference ** 2 # Negatives cancels out & big disagreements count more
            shared_movies += 1

    if shared_movies == 0:
        return 0

    return 1 / (1 + total) # adding one to the total prevents division by zero & caps the result at 1.0
