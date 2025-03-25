from flask import (Flask,render_template)
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)


@app.route('/')
def hello():
  return '<h1>Flask App</h1><p>afaik</p><p>idk</p>'

@app.route('/ethan')
def template():
  return render_template('template.html')

# Link to repository on github
# https://github.com/EthanPeregoy/CST205-Lab15