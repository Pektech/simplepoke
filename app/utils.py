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













