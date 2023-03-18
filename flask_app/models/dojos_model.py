from flask_app.config.mysqlconnections import connectToMySQL
from flask_app import DATABASE
from flask_app.models import ninjas_model

class Dojo:
    def __init__( self, data ):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.ninja_list = []


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL( DATABASE ).query_db(query)
        all_dojos = []
        for row in results:
            all_dojos.append( cls(row) )
        return all_dojos
    
    @classmethod
    def get_one(cls, id):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        result = connectToMySQL( DATABASE ).query_db(query, {"id" : id})
        return cls(result[0])
    
    @classmethod
    def create_one( cls, data ):
        query  = "INSERT INTO dojos( name ) "
        query += "VALUES( %(name)s );"

        result = connectToMySQL( DATABASE ).query_db( query, data )
        return result
    

    @classmethod
    def get_one_with_ninjas( cls, data ):
        query  = "SELECT * "
        query += "FROM dojos "
        query += "LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id "
        query += "WHERE dojos.id = %(id)s;"

        results = connectToMySQL( DATABASE ).query_db( query, data )
        print(results)
        current_dojo = cls( results[ 0 ] )

        for row in results:
            current_ninja = {
                "id": row["ninjas.id"],
                "first_name" : row[ "first_name" ],
                "last_name" : row[ "last_name" ],
                "age" : row[ "age" ],
                "created_at": row["ninjas.created_at"],
                "updated_at": row["ninjas.updated_at"]
            }
            current_ninja_object = ninjas_model.Ninja( current_ninja )
            current_dojo.ninja_list.append( current_ninja_object )
        print( "Ninjas", current_dojo.ninja_list )
        print(current_dojo.ninja_list)
        return current_dojo
    