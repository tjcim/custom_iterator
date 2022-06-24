from flask import Flask, render_template, abort

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/<date>|<index>|<store>")
def invoice(date, index, store):
    if date == "20220426" and index == "23" and store == "02":
        return render_template("winner.html")
    elif date == "20211105" and index == "22" and store == "03":
        return render_template("example.html")
    else:
        abort(404)
