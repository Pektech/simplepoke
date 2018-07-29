from app import app, db
from .forms import NewPoke
from flask import url_for, render_template, flash, redirect
from .models import Pokes
from sqlalchemy.exc import IntegrityError

@app.route('/test')
#@app.route('/index')
def index():
    return 'hello pek and monkey'


@app.route('/newpoke', methods=['POST', 'GET'])
def newpoke():
    form = NewPoke()
    if form.validate_on_submit():
        new_poke = Pokes(name=form.name.data, best_recipe=form.best_recipe.data,
                         percent=form.percent.data, info=form.info.data,
                         attracted=form.attracted.data)
        try:
            db.session.add(new_poke)
            db.session.commit()
            flash('Added {} {} {} {} {} {}'.format(new_poke.id,new_poke.name, new_poke.best_recipe,
                                         new_poke.percent, new_poke.info,
                                                new_poke.attracted), 'success' )
            return redirect('/newpoke')
        except IntegrityError as err:
            flash('Error {}'.format(err.orig.args), 'error')

    return render_template('newpoke.html', form = form)