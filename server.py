from flask import Flask, render_template

app = Flask(__name__)
print(__name__)


@app.route("/")
def my_home():
    # MUST KEEP FILES IN "templates" FOLDER
    return render_template('index.html')


@app.route("/intro")
def intro():
    # MUST KEEP FILES IN "templates" FOLDER
    return render_template('about.html')


@app.route("/work")
def work():
    return "<p>This is my work</p>"


@app.route("/about")
def about():
    return "<p>This is my about</p>"

@app.route("/#contact")
def contact():
    return "<p>This is my contact</p>"