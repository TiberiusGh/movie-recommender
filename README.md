# Movie Recommender

A movie recommendation system based on user-based collaborative filtering. Pick a user and a similarity measure, and the app finds the most similar users and predicts which movies the selected user would rate highest.

Built as coursework for 2DV515 – Web Intelligence at Linnaeus University.

## Features

- **Similar users:** ranks every other user by how closely their ratings match the selected user.
- **Recommendations:** predicts a score for each unseen movie as a similarity-weighted average of other users' ratings.
- **Two similarity measures**, selectable from the GUI:
  - **Euclidean distance:** similarity based on how far apart two users' ratings are on shared movies.
  - **Pearson correlation:** similarity based on whether two users' ratings move together, which compensates for users who rate consistently high or low.
- **REST API** with a static frontend served by the same Flask app.

## Tech stack

- **Backend:** Python 3.13, Flask, Gunicorn, managed with [uv](https://docs.astral.sh/uv/)
- **Frontend:** HTML, CSS and vanilla JavaScript
- **Deployment:** Docker

## Running locally

With uv:

```bash
cd backend
uv sync
uv run flask --app app run --debug --port 5001
```

Then open <http://localhost:5001>.

With Docker:

```bash
docker build -t movie-recommender .
docker run --rm -p 8000:8000 movie-recommender
```

Then open <http://localhost:8000>.

## API

| Endpoint | Description |
|---|---|
| `GET /api/users` | All users |
| `GET /api/users/<id>/similarusers?algorithm=euclidean\|pearson` | Users ranked by similarity |
| `GET /api/users/<id>/recommendations?algorithm=euclidean\|pearson` | Movies ranked by predicted score |

## Dataset

The app uses the [MovieLens](https://grouplens.org/datasets/movielens/) `ml-latest-small` dataset (610 users, 9,742 movies, 100,836 ratings), converted to a semicolon-separated format. MovieLens users are anonymous, so the user names are randomly generated.

> F. Maxwell Harper and Joseph A. Konstan. 2015. The MovieLens Datasets: History and Context. *ACM Transactions on Interactive Intelligent Systems (TiiS)* 5, 4: 19:1–19:19. <https://doi.org/10.1145/2827872>

The dataset is provided by [GroupLens Research](https://grouplens.org) at the University of Minnesota and is used here for non-commercial purposes under its [usage license](https://files.grouplens.org/datasets/movielens/ml-latest-small-README.html). This project is not endorsed by GroupLens or the University of Minnesota.
