from flask import Flask, render_template, request, session,  redirect

app = Flask(__name__)
app.secret_key = "keytosuccess__DJ khaled"

@app.route('/')
def index ():
    return render_template('index.html')


@app.route('/process', methods=["POST"])
def process():
    if request.form['action'] == "register":
        session['statement'] = "you are in register page"
    else:
        session['statement'] = "you are in login page"
    session["email"] = request.form["email"]
    session["password"] = request.form["password"]
    return render_template('process.html')

app.run(debug=True)