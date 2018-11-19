from flask import Flask, render_template,redirect, url_for, request, session, redirect, escape
app = Flask(__name__)
app.secret_key = 'amy'

@app.route('/')
def index():
	if 'username' in session:
		u = session['username']
		return render_template("index.html", uname=u)
	return render_template("index.html", uname='waht')


@app.route("/page")
def page1():
	return "Hi Amy, Finish your lab"

@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if str(request.form['username']) != 'admin' or str(request.form['password']) != "password":
			error = 'Wrong username or password.'
		else:
			session['usermame'] = request.form['username']
			return redirect(url_for('index'))
	return render_template('login.html', error=error)

@app.route('/logout')
def logout():
   session.pop('username', None)
   return redirect(url_for('index'))

if __name__ == '__main__':
	 app.run(debug=True)
