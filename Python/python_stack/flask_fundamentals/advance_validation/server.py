from flask import Flask, render_template, redirect, session, request, flash
import re


app = Flask(__name__)
email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app.secret_key = "yourmpmisawhore"
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=["POST"])
def process():
    if len(request.form['email']) < 1 :
        flash("email can no be blank!")
    elif not email_regex.match(request.form['email']):
        flash("you enter a invalid email")
    else:
        flash("success!")
    return redirect('/')

app.run(debug=True)