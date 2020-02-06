from flask import Flask, render_template, request, redirect, url_for, session
from sqlalchemy.exc import IntergrityError

from models import add_user, check_user

app = Flask(__name__)
app.secret_key = 'olujnybhgtvolimujhbtgv'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        repassword = request.form['repassword']
        if password != repassword:
            return render_template('index.html', error='repass_error')
        try:
            add_user(name, email, password)
        except IntegrityError:
            return render_template('index.html', error='db_error')
        session['username'] = name

        return redirect(url_for('user_page', name=name))
    return render_template('index.html')


@app.route('/users/<name>', method=['GET', 'POST'])
def user_page(name):
    if request.method == 'POST':
        title = request.form['title']
        details = request.form['details']
        deadline_date = request.form['deadline_date']
        add_task(title, details, deadline_date)
    return render_template('users.html', username=name)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = check_user(email, password)
        if user:
            session['username'] = user.name
            return redirect(url_for('user_page', name=user.name))
        else:
            render_template('login.html', error=True)
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


app.run(debug=True)
