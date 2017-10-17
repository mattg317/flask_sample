from flask import Flask, render_template

app = Flask("__main__")

@app.route("/")
def home():
    print("Retrieving homepage")
    return render_template("index.html")


@app.route("/about")
def about():
    print("Retrieving about page")
    return "Hey There"


if __name__ == ("__main__"):
    app.run(debug=True)
