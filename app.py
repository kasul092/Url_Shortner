import sqlite3
from hashids import Hashids
from flask import Flask, redirect, url_for, render_template, flash, request


def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


app = Flask(__name__)
app.config['SECRET_KEY'] = "this should be a secret random string"

hashids = Hashids(min_length = 4, salt = app.config["SECRET_KEY"])


@app.route("/", methods = ("GET", "POST"))
def Index():
    conn = get_db_connection()

    if request.method == "POST":
        url = request.form["url"]

        if not url:
            flash("The URL is required!")
            return redirect(url_for("index"))
        
        url_data = conn.execute("INSERT INTO urls (original url) VALUES (?)",(url, ))
        conn.commit()
        conn.close()

        url_id = url_data.lastrowid
        hashid = hashids.encode(url_id)
        short_url = request.host_url + hashid

        return render_template("index.html", short_url = short_url)

    return render_template("index.html")

@app.route("/<id>")
def url_redirect(id):
    conn = get_db_connection()

    original_id = hashids.decode(id)
    if original_id:
        original_id = original_id[0]
        url_data = conn.execute("SELECT original_url, clicks FROM urls"
                            "WHERE id = (?)", (original_id,)).fetchone()
        original_url = url_data["original_url"]
        clicks = url_data["clicks"]

        conn.execute("UPDATE urls SET clicks = ? WHERE id = ?",
                      (clicks+1 , original_id))

        conn.commit()
        conn.close()
        return  redirect(original_url)
    else:
        flash("Invalid URL")
        return redirect(url_for("index"))

