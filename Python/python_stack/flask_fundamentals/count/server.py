from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
app.secret_key = "keytosuccess"


@app.route('/')
def index():
    if "number" not in session:
        session["number"] = 0
    else:
        session["number"] += 1
    return render_template('index.html')


@app.route('/second', methods=['POST'])
def second():
    session["number"] += 1
    return redirect('/')


@app.route('/reset', methods=['POST'])
def reset():
    session["number"] = 0
    return redirect('/')


app.run(debug=True)