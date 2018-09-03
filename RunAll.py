from flask import Flask, render_template, request, session, redirect, url_for
import sqlite3

# to run:
# cd to directory
# source env/bin/activate
# export FLASK_APP=run.py; export FLASK_DEBUG=1
# flask run

app = Flask(__name__)

FOODDB = 'foods.db'


@app.route('/')
def index():
  con = sqlite3.connect(FOODDB)
  con.close()

  return render_template('index.html', disclaimer='Y = present, N = not present, T = traces')

@app.route('/process', methods=["POST"])
def confirm():
  con = sqlite3.connect(FOODDB)

  table = None
  cats = ''

  for input in request.form:
    if input == 'Ftype':
        table = request.form[input]
    else:
        cats += request.form[input]
        cats += ' = "N" or '
        cats += request.form[input]
        cats += ' = "T" AND '

  cats = cats[0:-5]
  if len(cats) >= 1:
      q = 'SELECT * FROM %s WHERE %s' % (table,cats)
  else:
      q = 'SELECT * FROM %s ' % (table)
  cur = con.execute(q)

  display = []
  for row in cur:
      display.append(row)

  con.close()
  return render_template('process.html', disclaimer='Y = present, N = not present, T = traces', display=display)
