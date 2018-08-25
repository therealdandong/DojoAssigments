from flask import Flask, render_template, request, session, redirect
import random
app = Flask(__name__)
app.secret_key = "keytosuccess"


@app.route('/')
def index():
    if "result" not in session:
        session["result"] = random.randrange(1, 101)

    return render_template("index.html")


@app.route('/compare', methods=["POST"])
def compare():
    session['guess'] = request.form['user_input']
    if int(session['guess']) > session["result"]:
        session["statement"] = "too high"
    elif int(session['guess']) < session["result"]:
        session["statement"] = "too low"
    else:
        session["statement"] = "that is the number" + str(session["result"])
    return redirect('/')


@app.route('/reset', methods=["POST"])
def reset():
    session.clear()
    return redirect('/')


app.run(debug=True)

