#various helper functions#
from app import db
from .models import Pokes
import csv



#turn names of pokemons in to slots#
def poke_to_slots():
    with open('pokes.csv', 'w', newline='') as csvfile:
        pokewriter = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        pokename = Pokes.query.all()
        for name in pokename:
            pokewriter.writerow([name.name])


# updates new column recipe_type based on values in info column

def recipe_types():
    recipe_types = ['Special Recipe', 'Basic Recipe', 'Good Recipe',
                   'Very Good Recipe', 'Good and Expensive',
                   'Very Good and Expensive']
    recipes = Pokes.query.all()
    for recipe in recipes:
        for item in recipe_types:
            if item in recipe.info:
                recipe.recipe_type = item
                recipe.info = recipe.info.split(item, 1)[-1]
                db.session.commit()










