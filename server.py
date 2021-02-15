from flask import Flask
from flask import render_template, redirect

app = Flask(__name__)


@app.route('/')
def initial():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
