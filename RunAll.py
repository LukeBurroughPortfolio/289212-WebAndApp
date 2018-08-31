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
    BurgerWrapPies = []
    cur = con.execute('SELECT Name,Gluten,Eggs,Soy,Fish_crust,peanuts,tree_nuts,sesame_seeds,sulphites,Lupin,Preservative,Flavour,Colours FROM Burgers')
    for row in cur:
        BurgerWrapPies.append(list(row))

    Breakfast = []
    cur = con.execute('SELECT Name,Gluten,Eggs,Soy,Fish_crust,peanuts,tree_nuts,sesame_seeds,sulphites,Lupin,Preservative,Flavour,Colours FROM breakfast')
    for row in cur:
        Breakfast.append(list(row))

    sides = []
    cur = con.execute('SELECT Name,Gluten,Eggs,Soy,Fish_crust,peanuts,tree_nuts,sesame_seeds,sulphites,Lupin,Preservative,Flavour,Colours FROM sides')
    for row in cur:
        sides.append(list(row))

    dessert = []
    cur = con.execute('SELECT Name,Gluten,Eggs,Soy,Fish_crust,peanuts,tree_nuts,sesame_seeds,sulphites,Lupin,Preservative,Flavour,Colours FROM dessert')
    for row in cur:
        dessert.append(list(row))

    drinks = []
    cur = con.execute('SELECT Name,Gluten,Eggs,Soy,Fish_crust,peanuts,tree_nuts,sesame_seeds,sulphites,Lupin,Preservative,Flavour,Colours FROM drinks')
    for row in cur:
        drinks.append(list(row))

    condiments = []
    cur = con.execute('SELECT Name,Gluten,Eggs,Soy,Fish_crust,peanuts,tree_nuts,sesame_seeds,sulphites,Lupin,Preservative,Flavour,Colours FROM condiments')
    for row in cur:
        condiments.append(list(row))

    return {'burgers':BurgerWrapPies, 'drinks':drinks, 'sides':sides, 'breakfast':Breakfast, 'dessert':dessert, 'condiments':condiments}

@app.route('/')
def index():
  con = sqlite3.connect(FOODDB)
  menu = FetchEverything(con)
  con.close()
  return render_template('index.html', disclaimer='Y = present, N = not present, T = traces')

@app.route('/order' methods=['POST'])
def index():
  con = sqlite3.connect(FOODDB)
  menu = FetchEverything(con)
  con.close()
  return render_template('order.html', disclaimer='Y = present, N = not present, T = traces', burgers=menu['burgers'], drinks=menu['drinks'], sides=menu['sides'], breakfasts=menu['breakfast'], desserts=menu['dessert'], condiments=menu['condiments'])
