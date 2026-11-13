from data_parser import ratings, movies
from euclidean import users_similarity

def recommendations(user_id, ratings, movies):
    similarities = users_similarity(user_id, ratings)
    results = []

    for movieID in movies:
        if movieID in ratings[user_id]:
            continue

        weighted_sum = 0
        similarity_sum = 0

        for similarity, other_user_id in similarities:
            # Skip users who can't help
            if similarity <= 0:
                continue
            if movieID not in ratings[other_user_id]:
                continue

            weighted_sum += similarity * ratings[other_user_id][movieID] # better than using average so that users with close similarity are given a better score
            similarity_sum += similarity

        if similarity_sum == 0:
            continue

        results.append((weighted_sum / similarity_sum, movieID))
    
    results.sort(reverse=True)
    return results