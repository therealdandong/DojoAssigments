from flask import Flask, session, render_template, request, flash, redirect

app = Flask(__name__)
app.secret_key = "keytosuccess"

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def result():
    session['name'] = request.form['name']
    session['email'] = request.form['email']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']

    if len(request.form['name']) < 1:
        flash("we want to know your name :)")
        return redirect('/')
    elif len(request.form['email']) < 1:
        flash("we want to know your email. :)")
        return redirect('/')
    elif len(request.form['location']) < 1:
        flash("we want to know your location. :)")
        return redirect('/')
    elif len(request.form['language']) < 1:
        flash("we want to know your favourite language. :)")
        return redirect('/')
    elif len(request.form['comment']) < 1 or len(request.form['comment']) > 121:
        flash("please leave your comment and don't excess 120 character. :)")
        return redirect('/')
    else:
        flash("thank you for your patient.")




    return render_template('result.html')

app.run(debug=True)