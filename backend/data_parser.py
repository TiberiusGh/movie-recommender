import csv
from pathlib import Path

DATASET = "movies_large"
DATASET_FILEPATH = Path(__file__).resolve().parent.parent / "data" / DATASET

def load_ratings():
    ratings = {}
    with open(DATASET_FILEPATH / "ratings.csv", newline="") as file:
        for row in csv.DictReader(file, delimiter=";"):
            user_id = int(row["UserId"])
            movie_id = int(row["MovieId"])
            rating = float(row["Rating"])

            if user_id not in ratings:
                ratings[user_id] = {}

            ratings[user_id][movie_id] = rating

    return ratings


def load_users():
    users = {}

    with open(DATASET_FILEPATH / "users.csv", newline="") as file:
        for row in csv.DictReader(file, delimiter=";"):
            user_id = int(row["UserId"])
            users[user_id] = row["Name"]

    return users


def load_movies():
    movies = {}

    with open(DATASET_FILEPATH / "movies.csv", newline="") as file:
        for row in csv.DictReader(file, delimiter=";"):
            movie_id = int(row["MovieId"])
            movies[movie_id] = row["Title"]

    return movies


ratings = load_ratings()
users = load_users()
movies = load_movies()
