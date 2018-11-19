from flask import Flask, render_template,redirect, url_for, request, session, redirect, escape, abort
app = Flask(__name__)
app.secret_key = 'amy'

usernameKey = 'username'
passwordKey = 'password'

@app.route('/')
def index():
	return render_template("index.html")


@app.route("/page")
def page1():
	if usernameKey in session:
		return 'the good stuff' + usernameKey
	return abort(418)

@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if str(request.form[usernameKey]) != 'admin' or str(request.form[passwordKey]) != "password":
			error = 'Wrong username or password.'
		else:
			session[usernameKey] = request.form[usernameKey]
			return redirect(url_for('page1'))
	return render_template('login.html', error=error)

@app.route('/logout')
def logout():
   session.pop(usernameKey, None)
   return redirect(url_for('index'))

@app.errorhandler(418)
def imATeapot(e):
    return render_template('418.html'), 418

if __name__ == '__main__':
	 app.run(debug=True)
