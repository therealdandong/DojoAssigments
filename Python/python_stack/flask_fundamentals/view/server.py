from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/<name>')
def index(name):
    return render_template('index.html', name=name, time = 11 )
app.run(debug=True)