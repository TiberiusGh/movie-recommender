from pathlib import Path
from flask import Flask
from data_parser import ratings, users, movies
from recommendation import recommendations

test = recommendations(3, ratings, movies)
print(test)

PROJECT_ROOT = Path(__file__).resolve().parent.parent

app = Flask(__name__, static_folder=PROJECT_ROOT / "web", static_url_path="")

@app.route("/")
def index():
    return app.send_static_file("index.html")




if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)

