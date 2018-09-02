from flask import Flask, render_template, request, session, redirect, url_for
import sqlite3

# to run:
# cd to directory
# source env/bin/activate
# export FLASK_APP=run.py; export FLASK_DEBUG=1
# flask run

app = Flask(__name__)

FOODDB = 'foods.db'

def FetchEverything(con):
    details = {}
    items = {}
    Timer = {}
    for input in request.form:
      Timer[input] = 1

    for input in request.form:
        if input == 'Ftype':
            details[input] = request.form[input]
        elif len(items) > len(Timer) - 1 :
            items[input] = " ("+request.form[input]+" != 'N') and"
        else:
            items[input] = " ("+request.form[input]+" != 'N')"
    Catagory = "".join(items)
    table = "".join(details)
    Display = []
    cur = con.execute( 'SELECT * FROM %s WHERE %s' % (table, Catagory) )

    for row in cur:
        Display.append(list(row))
    return {'display': Display}

@app.route('/')
def index():
  con = sqlite3.connect(FOODDB)
  con.close()

  return render_template('index.html', disclaimer='Y = present, N = not present, T = traces')

@app.route('/process', methods=["POST"])
def confirm():

  con = sqlite3.connect(FOODDB)
  food = FetchEverything(con)
  con.close()

  return render_template('process.html', disclaimer='Y = present, N = not present, T = traces', display=food['display'])
