from flask import Flask, render_template, redirect, url_for, request
from forms import addIngredientForm
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ingredients.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'badPassword'

db = SQLAlchemy(app)

class Ingredient(db.Model):
    upc = db.Column(db.Integer, primary_key = True, index = True)
    brand = db.Column(db.String(50), index = True, unique = False)
    ingredient_name = db.Column(db.String(80), index = True, unique = False)
    serving_size = db.Column(db.Integer, index = False, unique = False)
    serving_unit = db.Column(db.String(10), index = False, unique = False)
    ingredient_calorie = db.Column(db.Integer, index = True, unique = False)
    protein_grams = db.Column(db.Integer, index = False, unique = False)
    carb_total = db.Column(db.Integer, index = False, unique = False)
    carb_fiber = db.Column(db.Integer, index = False, unique = False)
    ingredient_fat = db.Column(db.Integer, index = False, unique = False)
    ingredient_sodium = db.Column(db.Integer, index = False, unique = False)
    ingredient_onhand = db.Column(db.Integer, index = False, unique = False)


@app.route('/')
def index():
    return render_template("index.html")

@app.route("/ingredients")
def ingredients():
    return render_template("ingredients.html")

@app.route('/ingredients/addIngredient', methods=["GET", "POST"])
def addIngredient():
    add_ingredient = addIngredientForm()
    if add_ingredient.validate_on_submit():
        ingredient = Ingredient(upc = add_ingredient.ingredientUPC.data, brand = add_ingredient.ingredientBrand.data, ingredient_name = add_ingredient.ingredientName.data, 
        serving_size = add_ingredient.serving_size.data, serving_unit = add_ingredient.serving_unit.data, ingredient_calorie = add_ingredient.calories.data, 
        protein_grams = add_ingredient.protein.data, carb_total = add_ingredient.totalCarbs.data, carb_fiber = add_ingredient.fiberCarbs.data, ingredient_fat = add_ingredient.fat.data, 
        ingredient_sodium = add_ingredient.sodium.data, ingredient_onhand = add_ingredient.onhand.data)
        db.session.add(ingredient)
        db.session.commit()
        return redirect(url_for('addIngredient', _external=False))
    return render_template("addIngredient.html", template_form = add_ingredient)

@app.route("/ingredients/viewIngredients")
def viewIngredients():
    ingredients = Ingredient.query.all()
    return render_template('viewingredients.html', ingredients = ingredients)

@app.route('/ingredients/viewIngredients/<int:ingredient>', methods=['GET', 'POST'])
def viewIngredient(ingredient):
    ingredient_view = Ingredient.query.get(ingredient)
    if request.method == 'POST':
        if request.form['submit'] == 'Delete':
            db.session.delete(Ingredient.query.get(ingredient))
            db.session.commit()
            ingredients = Ingredient.query.all()

            return render_template('viewingredients.html', ingredients = ingredients)
        elif request.form['submit'] == 'Edit':
            pass
        else:
            pass
    elif request.method == "GET":
        return render_template('ingredient.html', ingredient = ingredient_view)



if __name__ == "__main__":
    app.run(port=5000, debug=True)