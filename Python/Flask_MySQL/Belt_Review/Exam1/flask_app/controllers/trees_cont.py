from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.trees_model import Tree
from flask_app.models.users_model import User

@app.route('/new/tree')
def new_tree():
    if "user_id" not in session:
        return redirect("/user/login")
    return render_template('new_tree.html')

@app.route('/new/tree/request', methods = ['POST'])
def tree_planted():
    if "user_id" not in session:
        return redirect("/user/login")
    data = {
        "user_id": session['user_id'],
        "species": request.form['species'],
        "location": request.form['location'],
        "reason": request.form['reason'],
        "date_planted": request.form['date_planted']
    }
    Tree.plant_tree(data)
    return redirect('/dashboard')

@app.route('/trees/<int:id>')
def see_tree(id):
    if "user_id" not in session:
        return redirect("/user/login")
    return render_template('view_tree.html', tree = Tree.get_id({'id' : id}))

@app.route('/edit/tree/<int:id>')
def edit_tree(id):
    if "user_id" not in session:
        return redirect("/user/login")
    return render_template('edit_tree.html', tree = Tree.get_id({'id' : id}))

@app.route('/edit/tree/process/<int:id>')
def edit_tree_process():
    if "user_id" not in session:
        return redirect("/user/login")
    data = {
        'id': id,
        'species': request.form['species'],
        'location': request.form['location'],
        'reason': request.form['reason'],
        'date_planted': request.form['date_planted']
    }
    Tree.update_tree(data)
    return redirect('/dashboard')

@app.route('/tree/destroy/<int:id>')
def destroy_recipe(id):
    if 'user_id' not in session:
        return redirect('/user/login')
    Tree.kill_tree({'id':id})
    return redirect('/dashboard')