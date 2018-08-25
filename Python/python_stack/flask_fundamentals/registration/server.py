from flask import Flask, render_template, session, redirect, flash,request
import re
from datetime import datetime


app = Flask(__name__)
app.secret_key = "keytosucess"

email_regx = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    if len(request.form['email']) < 1:
        flash("please don't leave your email blank", "error")
        return redirect('/')
    elif len(request.form['first_name']) < 1:
        flash("please don't leave your first name blank", "error")
        return redirect('/')
    elif len(request.form['second_name']) < 1:
        flash("please don't leave your second name blank", "error")
        return redirect('/')
    elif len(request.form['password']) < 1:
        flash("please don't leave your password blank", "error")
        return redirect('/')
    elif len(request.form['confirm_password']) < 1:
        flash("please confirm your password", "error")
        return redirect('/')
    elif request.form['first_name'].isdigit() or request.form['second_name'].isdigit():
        flash("please don't include any number in your name.", "error")
        return redirect('/')
    elif request.form['password'] != request.form['confirm_password']:
        flash("password don't match", "error")
        return redirect('/')
    if email_regx.match(request.form['email']):
        pass
    else:
        flash("please enter a valid email.", "error")
        return redirect('/')
    upper = False
    digit = False

    for char in request.form['password']:
        if char.isupper():
            upper = True
    for char in request.form['password']:
        if char.isdigit():
            digit = True
    if upper and digit:
        pass
    else:
        flash("you must include one upper case and one number")
        return redirect('/')



    flash(request.form['date'])
    return redirect('/')
"""if request.form['date'] > datetime.now():
            flash("invalid date of birth")
            return redirect('/')
            "you have successful register a new account."
"""

app.run(debug=True)