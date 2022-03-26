from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def Welcome():
    return "Welcome to the data science world"



if __name__ == "__main__":
    app.run(debug = True, port= 8080)
