from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/secret')
def secret():
    return "you found secret"

@app.route('/results', methods = ["GET", "POST"])
def results():
    userdata = dict(request.form)
    print(userdata)
    print(userdata['nickname'])
    output = model.shout(userdata['nickname'])
    return render_template('results.html', output = output)
