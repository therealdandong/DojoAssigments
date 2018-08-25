from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/money')
def money():
    return render_template("money.html")


app.run(debug=True)