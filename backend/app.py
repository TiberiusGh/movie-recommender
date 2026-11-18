from pathlib import Path
from flask import Flask, jsonify, request
from data_parser import ratings, users, movies
from recommendation import recommendations, users_similarity
from euclidean import euclidean_alg
from pearson import pearson_alg


PROJECT_ROOT = Path(__file__).resolve().parent.parent

app = Flask(__name__, static_folder=PROJECT_ROOT / "web", static_url_path="")


@app.route("/")
def index():
    return app.send_static_file("index.html")


@app.route("/api/users")
def get_users():
    user_lst = []

    for user_id, name in users.items():
        user = {"id": user_id, "name": name}
        user_lst.append(user)

    return jsonify(user_lst)


@app.route("/api/users/<user_id>/recommendations")
def get_recommendations(user_id):
    int_userID = int(user_id)

    algorithm = find_alg_from_query(request.args.get("algorithm"))
    if algorithm is None:
        return jsonify({"error": "algorithm query must be 'euclidean' or 'pearson'"}), 400
    
    recommended_movies = recommendations(int_userID, ratings, movies, algorithm)

    results = []
    for score, movie_id in recommended_movies:
        movie = {"movie_id": movie_id, "movie_name": movies[movie_id], "estimated_score": score}
        results.append(movie)

    return jsonify(results)


@app.route("/api/users/<user_id>/similarusers")
def get_similar_users(user_id):
    int_userID = int(user_id)

    algorithm = find_alg_from_query(request.args.get("algorithm"))
    if algorithm is None:
        return jsonify({"error": "algorithm query must be 'euclidean' or 'pearson'"}), 400
    
    similar_users_lst = users_similarity(int_userID, ratings, algorithm)

    results = []
    for similarity_score, user_id in similar_users_lst:
        result = {"similarity_score": similarity_score, "user_id": user_id, "user_name": users[user_id] }
        results.append(result)

    return jsonify(results)


def find_alg_from_query(algorithm_name):
    if algorithm_name == "euclidean":
        return euclidean_alg
    if algorithm_name == "pearson":
        return pearson_alg
    return None
