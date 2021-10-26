from flask import Flask, render_template, abort, jsonify, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("welcome.html", message="This is my populated content.")

@app.route("/garageview/<string:value>")
def garageview(value):
    return value

@app.route("/garage", methods=["GET", "POST"])
def garage():
    if request.method == "POST":
        input = request.form["inputText"]
        return redirect(url_for("garageview", value=input))
    else:
        return render_template("button was clicked.")