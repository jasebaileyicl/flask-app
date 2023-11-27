from flask import Flask, redirect, url_for, render_template

from dotenv import load_dotenv
import os

# load_dotenv()
# SECRET_KEY = os.getenv("MY_SECRET")
app = Flask(__name__)

if __name__ == "__main__":
    app.run()


@app.route("/")  # this sets the route to this page
def home():
    db_user = os.environ["SECRET"]  # "cccc"
    return render_template("index.html", text=db_user)
    # return "Hello! this is the main page <h1>HELLO2</h1>"  # some basic inl


@app.route("/<name>")
def hello_name(name):
    return f"hello {name}"


@app.route("/admin")
def admin():
    return redirect(url_for("home"))
