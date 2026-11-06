from flask import Flask, render_template

app = Flask(__name__)

games = [
    {"name": "Cricket Arena", "category": "Sports", "icon": "🏏"},
    {"name": "Block World", "category": "Adventure", "icon": "🧱"},
    {"name": "Speed Racers", "category": "Racing", "icon": "🏎️"},
    {"name": "Space Battle", "category": "Action", "icon": "🚀"}
]

@app.route("/")
def home():
    return render_template("index.html", games=games)

@app.route("/play/<game_name>")
def play(game_name):
    valid_games = [g["name"] for g in games]

    if game_name not in valid_games:
        return "Game not found!", 404

    if game_name == "Cricket Arena":
        return render_template("cricket_arena.html")

    return render_template("game.html", game=game_name)

if __name__ == "__main__":
    print("NexPlay is starting...")
    app.run(debug=True)