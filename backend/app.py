from pathlib import Path
from flask import Flask, jsonify
from data_parser import ratings, users, movies
from recommendation import recommendations


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

    recommended_movies = recommendations(int_userID, ratings, movies)

    results = []
    for score, movie_id in recommended_movies:
        movie = {"movie_id": movie_id, "movie_name": movies[movie_id], "extimated_score": score}
        results.append(movie)

    return jsonify(results)



if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=True)

