import re
from datetime import datetime
from cs50 import SQL
from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from functools import wraps

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

user_id = 0

db = SQL("sqlite:///data.db")

def make_hex(red, green, blue):
    return "#%02x%02x%02x" % (red, green, blue)


def login_required(f):
#Stolen from C$50 finance!!!! :-)
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated_function


def error(code, message):
    return render_template("error.html", code=code, message=message)

@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()
    if request.method == "GET":
        return render_template("login.html")
    username = request.form.get("username")
    password = request.form.get("password")
    if not username:
        return error("042", "Not even deep thought can find your username")
    if not password:
        return error("042", "Not even deep thought can find your password")
    user = db.execute("SELECT * FROM users WHERE username = ?", username)
    if user == []:
        return error("042", "Deep Thought does not recognize you. Try joining the cause")
    if user[0]["password"] != password:
        return error("045", "You are not the one who has authority over this vessel. (wrong password)")
    session["user_id"] = user[0]["id"]
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    username = request.form.get("username")
    password = request.form.get("password")
    again = request.form.get("again")
    if not username:
        return error("o42", "please put username")
    if not password:
        return error("o42", "please put password")
    if len(list(password)) < 8:
        return error("Stay Secure", "password must be at least 8 characters long")
    if again != password:
        return error("Mke", "Make an effort to remember your password")
    if db.execute("SELECT * FROM users WHERE username = ?", username) != []:
        return error("505 Sorry.....", "Be more creative with ur username :)")
    db.execute("INSERT INTO users (username, password) VALUES(?, ?)", username, password)
    return redirect("/")


@app.route("/logout")
@login_required
def logout():
    session.clear()
    return redirect("/")


@app.route("/")
@login_required
def index():
    return render_template("index.html", username=db.execute("SELECT username FROM users WHERE id = ?", session["user_id"])[0]["username"])


@app.route("/progress")
@login_required
def progress():
    progress_ = db.execute("SELECT COUNT(*) FROM colors")[0]["COUNT(*)"]
    return render_template("progress.html", progress=progress_)

@app.route("/name", methods=["GET", "POST"])
@login_required
def name():
   if request.method == "GET":
       return render_template("name.html")
   red, green, blue = request.form.get("red"), request.form.get("green"), request.form.get("blue")
   if not red or not green or not blue:
       return error("042", "Missing color values")
   try:
       red = int(red)
       green = int(green)
       blue = int(blue)
   except ValueError:
       return error("045", "Values must be integers.")
   for vaal in [red, green, blue]:
       if not 0 <= vaal <= 255:
           return error("045", "Values must be in range 0-255.")
   return redirect(f"/colorpage?red={red}&green={green}&blue={blue}")

@app.route("/colorpage", methods=["GET", "POST"])
@login_required
def colorpage():
    red = request.args.get("red")
    green = request.args.get("green")
    blue = request.args.get("blue")
    if not red or not green or not blue:
        return error("red, green and blue args must exist")
    official_named = db.execute("SELECT officialnamed FROM colors WHERE red = ? AND green = ? AND blue = ?", red, green, blue)
    if official_named == []:
        official_named = 0
    else:
        official_named = official_named[0]["officialnamed"]
    winner = db.execute("SELECT name FROM color_candidates WHERE red = ? AND green = ? AND blue = ? ORDER BY votes DESC LIMIT 1", red, green, blue)
    if winner != []:
        winner = winner[0]["name"]
    else:
        winner = ""
    if official_named == 0:
        db.execute("UPDATE colors SET name = ? WHERE red = ? AND green = ? AND blue = ?", winner, red, green , blue)
    try:
        red = int(red)
        green = int(green)
        blue = int(blue)
    except ValueError:
        return error("042", "colors must have integer values")
    if not (0 <= red <= 255 and 0 <= green <= 255 and 0 <= blue <=255):
        return error("042", "This color does not exist.")
    names = db.execute("SELECT name FROM color_candidates WHERE red = ? AND green = ? AND blue = ?", red, green , blue)
    hexa = make_hex(red, green, blue)
    if request.method == "GET":
        return render_template("colorpage.html", names=names, hex=hexa, name_=winner, named=official_named)
    if request.form.get("mode_vote") == "":
        if db.execute("SELECT * FROM votes WHERE red = ? AND green = ? AND blue = ? AND id = ?", red, green, blue, session["user_id"]) != []:
            return error("240", "You have already voted for a name of this color.")
        decision = request.form.get("decision")
        if not decision:
            return error("042", "Please select an option")
        candidate = db.execute("SELECT * FROM color_candidates WHERE namer_id = ? AND red = ? AND green = ? AND blue = ?", session["user_id"], red, green, blue)
        db.execute("INSERT INTO votes (id, red, green, blue) VALUES(?, ?, ?, ?)", session["user_id"], red, green, blue)
        db.execute("UPDATE color_candidates SET votes = ? WHERE red = ? AND green = ? AND blue = ? AND namer_id = ?", candidate[0]["votes"] + 1, red, green, blue, session["user_id"])
    elif request.form.get("mode_name") == "":
        if db.execute("SELECT * FROM color_candidates WHERE red = ? AND green = ? AND blue = ? AND namer_id = ?", red, green, blue, session["user_id"]) != []:
            return error("240", "You have already given this color a name!")
        name = request.form.get("name")
        if not name:
            return error("042", "Missing color name.")
        for c in db.execute("SELECT name FROM color_candidates"):
            if c == name:
                return error("240", "A color with this name already exists.")
        db.execute("INSERT INTO color_candidates (name, red, green, blue, namer_id, votes) VALUES(?, ?, ?, ?, ?, 0)", name, red, green, blue, session["user_id"])
    return redirect(f"/colorpage?red={red}&green={green}&blue={blue}")

@app.route("/my_colors")
@login_required
def mycolors():
    return render_template("mycolors.html", colors=db.execute("SELECT * FROM color_candidates WHERE namer_id = ?", session["user_id"]))