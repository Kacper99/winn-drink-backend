from flask import Flask, Response
import json
import random

app = Flask(__name__)


def read_cards_file(file_name):
    with open("cards.json") as json_file:
        data = json.load(json_file)
        print(data)
        return data


cards = []


@app.route("/")
def health_check():
    return Response(
        "Healthy",
        mimetype="text/plain",
        status=200
    )

# application/json
@app.route("/cards")
def get_cards():
    random.shuffle(cards)
    return Response(
        json.dumps(cards),
        mimetype="application/json",
        status=200
    )


if __name__ == "__main__":
    cards = read_cards_file("cards.json")
    app.run(host="0.0.0.0", port=5000, debug=True)