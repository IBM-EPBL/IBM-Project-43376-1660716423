from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/blog")
def blog():
    return"My Blog"

@app.route('/signup')
def signup():
    return render_template ("signup.html")



@app.route('/signin')
def signin():
    return render_template ("signin.html")


if __name__ =  "__main__":
    app.run(debug=True)