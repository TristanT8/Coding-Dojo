from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask_app import bcrypt
db = "arbortrary"

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_user(cls, form_data):
        hash_password = bcrypt.generate_password_hash(form_data['password'])
        user_data = {
            "first_name": form_data['first_name'],
            "last_name": form_data['last_name'],
            "email": form_data['email'],
            "password": hash_password
            }
        query = 'INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);'
        result = connectToMySQL('arbortrary').query_db(query, user_data)
        return result

    '''@classmethod
    def get_users(cls):
        query = "SELECT * FROM users"
        results = connectToMySQL("arbortrary").query_db(query)
        print (f'getallusers() from model {results}')
        users_list = []
        for user in results:
            users_list.append(cls(user))
        return users_list

    @classmethod
    def get_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(db).query_db(query,data)
        if not result:
            return False
        return cls(result[0])

    @classmethod
    def specific_user(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL('arbortrary').query_db(query,data)
        return cls(result[0])'''

    @staticmethod
    def validate_register(user_data):
        is_valid = True
        if len(user_data['first_name'])<2:
            flash("First Name must be at least 2 characters!", 'register')
            is_valid = False
        if len(user_data['last_name'])<2:
            flash("Last Name must be at least 2 characters!", 'register')
            is_valid = False
        if not EMAIL_REGEX.match(user_data['email']):
            flash("Invalid Email", 'register')
            is_valid = False
        if 'password' in user_data and 'confirm' in user_data:
            if user_data['password'] != user_data['confirm']:
                flash("Passwords don't match","register")
            is_valid = False
        if 'password' in user_data and len(user_data['password'])<8:
            flash("Password must be at least 8 characters", 'register')
            is_valid = False
        return is_valid

    @staticmethod
    def validate_login(form_data):
        if not EMAIL_REGEX.match(form_data['email']):
            flash("Invalid email/password.","login")
            return False
        user = User.get_email(form_data)
        if not user:
            flash("Invalid email/password.","login")
            return False
        if not bcrypt.check_password_hash(user.password, form_data['password']):
            flash("Invalid email/password.","login")
            return False
        return user
