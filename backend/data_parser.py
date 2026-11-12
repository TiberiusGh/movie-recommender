import csv
from pathlib import Path

DATASET = "movies_example"
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

ratings = load_ratings()
