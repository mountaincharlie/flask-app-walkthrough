# imports
import os
from flask import Flask, render_template

# creating an instance of the Flask class with app module name as 1st arg
app = Flask(__name__)

# decorator ensures that nav to the root dir triggers the function after
@app.route("/")
def index():
    return render_template("index.html")


# creating the 'about' view (also linked in the html files)
@app.route("/about")
def about():
    return render_template("about.html", page_title="About")

# contact view
@app.route("/contact")
def contact():
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


# __main__ = name of default python module
if __name__ == "__main__":
    # getting IP address and port or setting to defaults

    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)  # CHANGE to False before deployment!!!
