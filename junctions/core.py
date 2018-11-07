import argparse

from flask import Flask, jsonify


app = Flask(__name__)

# ToDo move this into a database
coordinates_db = [
    {
        "id": 0,
        "coordinates": [-77.60431855916977, 43.15761560347455],
        "intersection": "E Main St, East Ave and Franklin St",
        "thumbs_up": 5,
        "thumbs_down": 0,
    },
    {
        "id": 1,
        "coordinates": [-77.60634899139404, 43.15714797334406],
        "intersection": "E Main St and Clinton Ave",
        "thumbs_up": 5,
        "thumbs_down": 0,
    },
]

coordinate_comments = {
    0: [
        {"user": "skroh", "comment": "I nearly died here."},
        {"user": "skroh", "comment": "This is the intersection that started it all."},
    ],
    1: [],
}


@app.route("/v0/coordinates")
def get_coordinates():
    return jsonify(coordinates_db)


@app.route("/v0/coordinate/<int:junction_id>/comments")
def get_coordinate_comments(junction_id):
    if junction_id not in coordinate_comments:
        return jsonify([]), 404
    else:
        return jsonify(coordinate_comments[junction_id])


@app.route("/")
def hello():
    response_body = "Hello World! <br/><br/>" + "Welcome to Junctions.io <br/>"

    return response_body


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=5000)
    parser.add_argument("--host", default="127.0.0.1")
    args = parser.parse_args()
    app.run(port=args.port, host=args.host)
