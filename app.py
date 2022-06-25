from flask import Flask, render_template, abort

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/<date>|<index>|<store>")
def invoice(date, index, store):
    if date == "20220421" and index == "24" and store == "04":
        return render_template("winner.html", _date=date, index=index, store=store)
    elif date == "20211105" and index == "22" and store == "03":
        return render_template("example.html")
    else:
        abort(404)
