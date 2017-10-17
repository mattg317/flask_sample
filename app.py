from flask import Flask

app = Flask("__main__")

@app.route("/")
def home():
    print("Retrieving homepage")
    return "Welcome to my home page"


@app.route("/about")
def about():
    print("Retrieving about page")
    return app.send_static_file('index.html')


if __name__ == ("__main__"):
    app.run()
