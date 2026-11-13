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



def users_similarity(user_id, ratings):
    similarities = []

    for curr_userID in ratings:
        if curr_userID == user_id:
            continue

        similarity_score = euclidean_alg(ratings[user_id], ratings[curr_userID])
        similarities.append((similarity_score, curr_userID))

    sorted_lst = sorted(similarities, reverse=True)

    return sorted_lst