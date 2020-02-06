from flask import Flask, request, redirect, url_for, render_template, session

app = Flask(__name__)

@app.route('/')
def index():
    role = 'author'
    return render_template('index.html', role=role)

app.run(debug=True)    