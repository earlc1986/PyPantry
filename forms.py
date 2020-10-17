from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class addIngredientForm(FlaskForm):
    ingredientUPC = StringField("UPC:", validators=[DataRequired()])
    ingredientBrand = StringField("Brand Name:")
    ingredientName = StringField('Ingredient Name:', validators=[DataRequired()])
    serving_size = StringField('Serving Size:', validators=[DataRequired()])
    serving_unit = StringField('Serving Unit:', validators=[DataRequired()])
    calories = StringField('Calories Per Serving:', validators=[DataRequired()])
    protein = StringField('Protein (In Grams):', validators=[DataRequired()])
    totalCarbs = StringField('Total Number of Carbs:', validators=[DataRequired()])
    fiberCarbs = StringField("Carbs From Fiber:", validators=[DataRequired()])
    fat = StringField("Fat (In Grams):", validators=[DataRequired()])
    sodium = StringField("Sodium (In Milligrams):", validators=[DataRequired()])
    onhand = StringField("Number Currently On Hand:", validators=[DataRequired()])
    submit = SubmitField('Submit')


