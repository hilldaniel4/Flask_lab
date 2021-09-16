from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/<name>")
def hello_name(name):
    return "Hello "+ name

if __name__ == "__main__":
    app.run(debug=True)     