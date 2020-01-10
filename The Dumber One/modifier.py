from flask import Flask,render_template,json,url_for,redirect
app = Flask(__name__)
label = "sad"
usrInput = True

@app.route("/happy")
def happy():
    return render_template('happy.html')
@app.route("/sad")
def sad():
    return render_template('sad.html')
@app.route("/disgust")
def disgust():
    return render_template('disgust.html')
@app.route("/neutral")
def neutral():
    return render_template('neutral.html')
@app.route("/suprising")
def suprising():
    return render_template('suprising.html')
@app.route("/angry")
def angry():
    return render_template('angry.html')
@app.route("/scared")
def scared7():
    return render_template('scared.html')
@app.route("/")
def hello():
    if label == "happy":
        return redirect(url_for('happy'))
    if label == "sad":
        return redirect(url_for('sad'))
    if label == "disgust":
        return redirect(url_for('disgust'))
    if label == 'neutral':
        return redirect(url_for('neutral'))
    if label == 'suprising':
        return redirect(url_for('suprising'))
    if label == 'angry':
        return redirect(url_for('angry'))
    if label == 'scared':
        return redirect(url_for('scared'))
if __name__ == "__main__":
    app.run(debug=True)
