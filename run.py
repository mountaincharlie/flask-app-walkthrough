# imports
import os
import json
# 'render_template' is to render a template, 'request' is to allow different reqest methods such as POST, 'flash' is for displaying non-permenant messages to user
from flask import Flask, render_template, request, flash
if os.path.exists("env.py"):
    import env

# creating an instance of the Flask class with app module name as 1st arg
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")

# decorator ensures that nav to the root dir triggers the function after
@app.route("/")
def index():
    return render_template("index.html")


# creating the 'about' view (also linked in the html files)
@app.route("/about")
def about():
    data = []
    # opening the json file with the company data
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


# view for about members (the <> pass data from the url)
@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    # 1st 'member' is var passed into the .html, 2nd is the var defined above
    return render_template("member.html", member=member)


# contact view (with argument for route to accept POST method)
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have recieved your message!".format(
            request.form.get("name")))
        # [] notaion throws exceptions if no key
        # print(request.form['name'])
        # print(request.form['email'])  
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
