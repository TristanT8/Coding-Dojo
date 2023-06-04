from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.users_model import user
from flask import flash

class Tree:
    def __init__(self, tree_data):
        self.id = tree_data['id']
        self.species = tree_data['species']
        self.location = tree_data['location']
        self.reason = tree_data['reason']
        self.date_planted = tree_data['date_planted']
        self.user_id = tree_data['user_id']
        self.planter = None

    @classmethod
    def all_info(cls):
        query = "SELECT * FROM trees JOIN users on trees.user_id = users.id;"
        results = connectToMySQL('arbortrary_schema').query_db(query)
        print(results)
        user_tree = cls(results[0])
        for tree in results:
            tree_info = {
                "id" : tree['user_id'],
                "first_name" : tree['first_name'],
                "last_name" : tree['last_name'],
                "email" : tree['email'],
                "password" : "",
                "created_at" : tree['created_at'],
                'updated_at' : tree['updated_at']
            }
            user_tree.planter.append(Tree(tree_info))
            return user_tree

    @classmethod
    def get_id(cls,data):
        query = "SELECT * FROM trees JOIN users on trees.user_id = users_id WHERE trees.id = %(id)s;"
        result = connectToMySQL('arbortrary_schema').query_db(query,data)
        if not result:
            return False
        
        result = result[0]
        trees = cls(result)
        tree_data = {
            "id": result['users.id'],
            "first_name": result['first_name'],
            "last_name": result['last_name'],
            "email": result['email'],
            "password": "",
            "created_at": result['users.created_at'],
            "updated_at": result['users.updated_at']
        }
        trees.planter = user.User(tree_data)
        return trees

    @classmethod
    def plant_tree(cls, form_data):
        query = "INSERT INTO trees (species, location, reason, date_planted, user_id) VALUES (%(species)s, %(location)s, %(reason)s, %(date_planted)s, %(user_id)s);"
        return connectToMySQL('arbortrary').query_db(query, form_data)

    @classmethod
    def update_tree(cls, form_data):
        query = "UPDATE trees SET species = %(species)s, location = %(location)s, reason = %(reason)s, date_planted = %(date_planted)s WHERE is = %(id)s;"
        return connectToMySQL('arbortrary').query_db(query, form_data)

    @classmethod
    def kill_tree(cls, data):
        query = "DELETE FROM trees WHERE id = %(id)s"
        return connectToMySQL('arbortrary').query_db(query, data)