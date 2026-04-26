from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Home Page"

@app.route("/about")
def about():
    return "About Page"

@app.route("/search")
def search():
    name = request.args.get("name")
    return f"Searching for {name}"

if __name__ == "__main__":
    app.run(debug=True)