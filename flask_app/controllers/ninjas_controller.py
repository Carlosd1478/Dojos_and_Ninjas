from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.ninjas_model import Ninja
from flask_app.models.dojos_model import Dojo

@app.route('/form')
def new():
    list_of_dojos = Dojo.get_all()
    return render_template("new_ninja.html", list_of_dojos = list_of_dojos)

@app.route( '/ninja/new', methods=['POST'] )
def create_ninja():
    new_ninja = {
        "first_name" : request.form[ 'first_name' ],
        "last_name" : request.form[ 'last_name' ],
        "age" : request.form[ 'age' ],
        "dojo_id" : request.form[ 'dojo_id' ]
    }
    Ninja.create_one( new_ninja )
    return redirect( '/dojos' )

