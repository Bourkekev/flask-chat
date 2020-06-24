import os
from datetime import datetime
from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)
app.secret_key = "randomstring567"
messages = []

def add_messages(username, message):
    """Adds the user and message to the messages list"""
    now = datetime.now().strftime("%H:%M:%S")
    messages.append("({}) {}: {}".format(now, username, message))


def get_all_messsages():
    """Get all messages and separate with a `br`"""
    return "<br>".join(messages)

@app.route('/', methods = ["GET", "POST"])
def index():
    """Main page with instructions"""

    if request.method == "POST":
        session["username"] = request.form["username"]

    if "username" in session:
        return redirect(session["username"])

    return render_template("index.html")


@app.route('/<username>')
def user(username):
    """Display chat messages"""
    return "<h1>Welcome {0}</h1>{1}".format(username, get_all_messsages())


@app.route('/<username>/<message>')
def send_message(username, message):
    """Create a new message and redirect back to chat page"""
    add_messages(username, message)
    return redirect("/" + username)


app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)