from flask import Flask
from flask import render_template,request
import sqlite3 as sql

app=Flask(__name__)

@app.route('/',methods=['POST','GET'])
def home():
	if request.method=='POST':
		username=request.form['username']
		password=request.form['password']
		insertUser(username,password)
		users = retriveUsers()
		return render_template('index.html',users=users)
	else:
		return render_template('index.html')


def insertUser(username,password):
	con = sql.connect("databases.db")
	cur = con.cursor()
	cur.execute("use user;INSERT INTO users (username,password) VALUES (?,?)", (username,password))
	con.commit()
	con.close()

def retriveUser():
	con = sql.connect("databases.db")
	cur = con.cursor()
	cur.execute("use user;SELECT username, password FROM users")
	users = cur.fetchall()
	con.close()
	return users

if __name__ == '__main__':
	app.run(debug=False,host='0.0.0.0')