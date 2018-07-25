from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, BooleanField
from wtforms.validators import DataRequired, ValidationError
from .models import Pokes


class NewPoke(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    attracted = BooleanField('Recipes work')
    best_recipe = StringField('Recipe')
    percent = IntegerField('%', default=0)
    info = TextAreaField('Info', default='This Pokemon does not have a favorite recipe')
    submit = SubmitField('Add')


    def validate_name(self, name):
        poke = Pokes.query.filter_by(name=name.data).first()
        if poke is not None:
            raise ValidationError('This pokemon is already in db')
