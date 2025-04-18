from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy #make a connection to the db  model
import os

# Manually fix the instance path to avoid mismatch
base_dir = os.path.abspath(os.path.dirname(__file__))
instance_dir = os.path.join(base_dir, 'instance')

# create an instance of Flask -
# Flask is a vew framework to present a webpage or API response
# Handels the routing of incoming request to an appropriate view function 
# and also returns the view functions# response to the client.
app = Flask(__name__, instance_path=instance_dir) #  Explicitly tell Flask to use the 'instance' folder

#Join the absolute path to make it bulletproof
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.instance_path, 'drinks.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
print("📂 Using database at:", app.config['SQLALCHEMY_DATABASE_URI'])
 
# pass the Flask instance in the db Model to make the connection between the app and the db
db = SQLAlchemy(app)

##create a data model
class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))
    
    def __repr__(self):
        return f"{self.name} - {self.description}"                       
                                

@app.route('/')
def index():
    return "Hello!"    

@app.route('/drinks')
def get_drinks():
    try:
        drinks = Drink.query.all()
        output = [{"name": drink.name, "description": drink.description} for drink in drinks]
        return {"drinks": output}   
        # output = []
        # for drink in drinks:
        #     drink_data = {"name": drink.name, "description": drink.description}
        #     output.append(drink_data)
        
    except Exception as e:   
        return {"error": str(e)}, 500
    
@app.route("/drinks/<id>")    
def get_drink(id):
    drink = Drink.query.get_or_404(id)
    return {"name": drink.name, "description": drink.description}

@app.route("/drinks", methods=["POST"])
def app_drink():
    drink = Drink(name=request.json['name'], description=request.json['description'])
    db.session.add(drink)
    db.session.commit()
    return {"id": drink.id}

@app.route("/drinks/<id>", methods=["DELETE"])
def delete_drinks(id):
    drink = Drink.query.get(id)
    if drink is None:
        return {"error": "not found"}
    db.session.delete(drink)
    db.session.commit()
    return {"message": f"Drink {id} deleted"}
    