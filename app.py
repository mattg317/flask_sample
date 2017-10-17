from flask import Flask, render_template

app = Flask("__main__")

@app.route("/")
def home():
    print("Retrieving homepage")
    return "Welcome to my home page"


@app.route("/about")
def about():
    print("Retrieving about page")
    return render_template('index.html')


if __name__ == ("__main__"):
    app.run()
