from flask_app.config.mysqlconnections import connectToMySQL
from flask_app import DATABASE
from flask_app.models import dojos_model

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    @classmethod
    def create_one(cls, data):
        query  = "INSERT INTO ninjas( first_name, last_name, age, dojo_id ) "
        query += "VALUES( %(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s ); "

        result = connectToMySQL( DATABASE ).query_db( query, data )
        return result