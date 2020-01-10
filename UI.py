from flask import Flask,render_template
app = Flask(__name__)
@app.route("/")
def hello():
    label = "happy" #This input is the actually from the model
    return render_template("modifier.html",val = label)


if __name__ == "main":
    app.run()
