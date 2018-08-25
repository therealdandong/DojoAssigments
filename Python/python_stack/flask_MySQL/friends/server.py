from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/friends/friend_id', methods=['POST'])
def create(friend_id):
    query = "SELECT * FROM friends WHERE id = :special_id"
    data = {"special_id" : "friend_id"}
    friends = mysql.query_db(query,data)
    return render_template("index.html", a_friend=friends[0])
app.run(debug=True)