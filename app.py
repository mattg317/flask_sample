from flask import Flask

app = Flask("__main__")

@app.route("/")
def home():
		print("Retrieving homepage")
		return "Welcome to my home page"

if __name__ == ("__main__"):
		app.run()
