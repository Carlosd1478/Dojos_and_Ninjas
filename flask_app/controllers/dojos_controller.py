from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.dojos_model import Dojo

@app.route( '/dojo/<int:id>', methods=['GET'] )
def get_dojo_by_id( id ):
    data = {
        "id" : id
    }
    current_dojo = Dojo.get_one_with_ninjas( data )
    return render_template( "show_dojo.html", dojo = current_dojo )

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def all_doj():
    all_dojos = Dojo.get_all()
    return render_template("dojos.html",all_dojos = all_dojos)

@app.route("/dojo/<int:dojo_id>")
def show(dojo_id):
    one_dojo = Dojo.get_one(dojo_id)
    return render_template("show_dojo.html", one_dojo = one_dojo)

@app.route( '/dojos/create', methods=['POST'] )
def create_dojo():
    print(request.form)
    Dojo.create_one( request.form )
    return redirect( '/dojos' )

