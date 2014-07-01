import markdown
from flask import Flask
from flask import render_template
from flask import Markup

app = Flask(__name__)
@app.route('/')

def index():
  f = open('sample.md', 'r')
  content = f.read()
  content = Markup(markdown.markdown(content))
  return render_template('index.html', **locals())

app.run(host='0.0.0.0')
