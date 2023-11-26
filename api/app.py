from flask import Flask, redirect, url_for,  render_template

app = Flask(__name__)

if __name__ == "__main__":
    app.run()


@app.route("/")  # this sets the route to this page
def home():
    return render_template("index.html", text="helxlo")
    #return "Hello! this is the main page <h1>HELLO2</h1>"  # some basic inl


@app.route("/<name>")
def hello_name(name):
    return f"hello {name}"


@app.route("/admin")
def admin():
    return redirect(url_for("home"))
