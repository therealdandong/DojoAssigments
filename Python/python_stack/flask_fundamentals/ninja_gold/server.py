from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = "MajoyKEYYYYY"


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/process', methods=['POST'])
def process():
    output = []
    if 'gold' not in session:
        session['gold'] = 0
    if request.form['deter'] == 'farm':
        a = random.randrange(10, 21)
        session['gold'] += a
        session['statement'] = ("earned " + str(a) + " in the farm\n")
    elif request.form['deter'] == 'cave':
        a = random.randrange(5, 11)
        session['gold'] += a
        session['statement'] = ("earned " + str(a) + " in the cave\n")
    elif request.form['deter'] == 'house':
        a = random.randrange(2, 6)
        session['gold'] += a
        session['statement'] = ("earned " + str(a) + " in the house\n")
    elif request.form['deter'] == 'casino':
        a = random.randrange(-50, 51)
        session['gold'] += a
        if a > 0:
            session['statement'] = ("earned " + str(a) + " in the casino\n")
        elif a < 0:
            session['statement'] = ("taken " + str(a*-1) + " in the casino\n")
    output += session['statement']
    return redirect('/')


app.run(debug=True)
