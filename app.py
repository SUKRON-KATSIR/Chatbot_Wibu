from process import preparation, generate_response
from flask import Flask, render_template, request, url_for


preparation()

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

@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

@app.route("/get")
def get_bot_response():
    user_input = str(request.args.get('msg'))
    result = generate_response(user_input)
    return result

if __name__ == "__main__":
    app.run(debug=True)
