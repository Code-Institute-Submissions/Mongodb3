import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from flask_paginate import Pagination
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from forms import RegisterForm, LoginForm, RecipeForm, EditRecipeForm,\
 DeleteForm
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


def find_recipes(offset=0, per_page=5):
    """
    function for pagination
    """
    return mongo.db.recipes.find()[offset: offset + per_page]


@app.route("/")
@app.route("/home")
def home():
    """
    function for home extent jinja base.html
    """
    return render_template("home.html")


@app.route('/allrecipes')
def allrecipes():
    """
    function for allrecipes extent jinja base.html.
    Users can find allrecipes upload by other users.
    """
    page = int(request.args.get('page', 1))
    per_page = 2
    offset = (page - 1) * per_page
    paginated_recipes = find_recipes(offset=offset, per_page=per_page)
    total = paginated_recipes.count()
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='materialize')
    return render_template("allrecipes.html", recipes=paginated_recipes,
                           page=page, per_page=per_page,
                           pagination=pagination)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    function for login extent jinja base.html.
    Users can  access website.
    """
    login_form = LoginForm()

    if login_form.validate_on_submit():
        found_username = mongo.db.users.find_one({'username':
                                                  request.form['username']})

        if found_username:
            existing_user = mongo.db.users.find_one({"username":
                                                     request.form.get(
                                                      "username")})
            if check_password_hash(existing_user["password"],
                                   request.form.get("password")):
                session["username"] = request.form.get("username")
                session['logged-in'] = True
                flash('Login successfully.', 'primary')
                return redirect(url_for("profile",
                                        username=session["username"]))

            else:
                flash('Password incorrect. Please try again.', 'danger')
                return redirect(url_for('login'))

        else:
            flash('Username not found. Please try again.', 'danger')
        return redirect(url_for('login'))

    return render_template('login.html', form=login_form)


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    function for register extent jinja base.html.
    Users have to register before login.
    """
    register_form = RegisterForm()

    if register_form.validate_on_submit():
        found_username = mongo.db.users.find_one({'username':
                                                  request.form['username']})

        if not found_username:
            hashed_pw = generate_password_hash(request.form.get("password"))
            mongo.db.users.insert_one({'username': register_form.username.data,
                                       'password': hashed_pw})
            session["username"] = request.form.get("username")
            return render_template('profile.html',
                                   username=session["username"])
        else:
            flash('Duplicate username detected. Please try again', 'danger')
            return redirect(url_for('register'))

    return render_template('register.html', form=register_form)


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """
    function for profile extent jinja base.html.
    Users have to register. Then can access their profile.
    """
    username = mongo.db.users.find_one(
        {"username": session["username"]})["username"]
    recipes = mongo.db.recipes.find()
    return render_template("profile.html", username=username, recipes=recipes)


@app.route("/logout")
def logout():
    """
    function for logout extent jinja base.html.
    Erase session from website.
    """
    flash("You have been logged out")
    session.clear()
    return redirect(url_for("home"))


@app.route('/addrecipe', methods=['GET', 'POST'])
def addrecipe():
    """
    function for addrecipe extent jinja base.html.
    Allow users to add recipes. Use wtfroms.
    """
    recipe_form = RecipeForm()

    if request.method == 'POST':
        mongo.db.recipes.insert_one({
            'username': session['username'],
            'recipe_name': recipe_form.recipe_name.data,
            'description': recipe_form.description.data,
            'ingredients': recipe_form.ingredients.data,
            'cooking_time': recipe_form.cooking_time.data,
            'calories': recipe_form.calories.data,
            'recipe_image': recipe_form.recipe_image.data,
        })
        flash('Recipe added.', 'primary')
        return render_template("profile.html")
    return render_template('newtask.html', form=recipe_form)


@app.route('/recipe_view/<recipe_id>')
def recipe_view(recipe_id):
    """
    function for recipe_view extent jinja base.html.
    User must be login.
    """
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template('recipe_view.html', recipe=recipe)


@app.route('/edit_recipe/<recipe_id>', methods=['GET', 'POST'])
def edit_recipe(recipe_id):
    """
    function for edit_recipe extent jinja base.html.
    User must be loged and has to be the creator of recipe.
    Furthermore, the recipe must exist.
    """
    recipe_edit = EditRecipeForm()
    recipe = mongo.db.recipes.find_one_or_404({'_id': ObjectId(recipe_id)})
    if request.method == 'POST':
        mongo.db.recipes.update_one({'_id': ObjectId(recipe_id)},
                                    {'$set':
                                    {
                                     'recipe_name': recipe_edit.
                                     recipe_name.data,
                                     'description': recipe_edit.
                                     description.data,
                                     'ingredients': recipe_edit.
                                     ingredients.data,
                                     'cooking_time': recipe_edit.
                                     cooking_time.data,
                                     'calories': recipe_edit.
                                     calories.data,
                                     'recipe_image': recipe_edit.
                                     recipe_image.data, }})
        flash('Recipe updated.', 'primary')
        return render_template("profile.html")

    elif request.method == 'GET':
        recipe_edit.recipe_name.data = recipe['recipe_name']
        recipe_edit.description.data = recipe['description']
        recipe_edit.ingredients.data = recipe['ingredients']
        recipe_edit.cooking_time.data = recipe['cooking_time']
        recipe_edit.calories.data = recipe['calories']
        recipe_edit.recipe_image.data = recipe['recipe_image']

    else:
        flash('Something went wrong...Recipe not updated.', 'primary')
        return redirect(url_for('profile'))

    return render_template('edit_recipe.html', form=recipe_edit, recipe=recipe)


@app.route('/delete_recipe/<recipe_id>', methods=['GET', 'POST'])
def delete_recipe(recipe_id):
    """
    function for delete_recipe extent jinja base.html.
    User must be loged and has to be the creator of recipe.
    Furthermore, the recipe must exist.
    """
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    recipe_delete = DeleteForm()
    if request.method == 'POST':
        if session['username'] == request.form.get('username'):
            mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
            flash('Recipe removed.', 'danger')
            return render_template("profile.html")
        else:
            flash('Error ocurred.', 'danger')
            return render_template("profile.html")

    return render_template('delete_recipe.html', form=recipe_delete,
                           recipe=recipe)


@app.errorhandler(404)
def response_404(exception):
    """
    function for handle exceptions.
    """
    return render_template('404.html', exception=exception)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
