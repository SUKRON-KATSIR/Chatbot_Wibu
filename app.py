from flask import Flask, render_template, request, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/budaya")
def budaya():
    return render_template("budaya.html")


@app.route("/wisata")
def wisata():
    return render_template("wisata.html")


if __name__ == "__main__":
    app.run(debug=True)
