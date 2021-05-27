import pyrebase # pip install pyrebase4
import os
from dotenv import load_dotenv
from routes import user, menu
from flask import Flask, jsonify, request, abort, Response
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

firebaseConfig = {
    'apiKey': os.getenv("apiKey"), 
    'authDomain': os.getenv("authDomain"),
    'databaseURL': os.getenv("databaseURL"),
    'projectId': os.getenv("projectId"),
    'storageBucket': os.getenv("storageBucket"),
    'messagingSenderId': os.getenv("messagingSenderId"),
    'appId': os.getenv("appId"),
    'measurementId': os.getenv("measurementId")
}

firebase=pyrebase.initialize_app(firebaseConfig)

db=firebase.database()

auth=firebase.auth()

# storage=firebase.storage()



@app.route('/', methods=['GET'])
def home():
    if request.method != 'GET': 
        return Response(status=404)
    return Response(status=200)

@app.route('/users', methods=['GET'])
def get_all_users_data():
    if request.method != 'GET': 
        return Response(status=404)
    
    return jsonify(user.get_all_users_data(db))

@app.route('/menu', methods=['GET'])
def get_menu_data():
    if request.method != 'GET': 
        return Response(status=404)
    return jsonify(menu.get_menu_data(db))

@app.route('/user/<id>', methods=['GET'])
def get_user_data_with_id(id):
    if request.method != 'GET': 
        return Response(status=404)

    return jsonify(user.get_user_data_with_id(db, id))

@app.route('/menu/<id>', methods=['GET'])
def get_menu_item_data_with_id(id):
    if request.method != 'GET': 
        return Response(status=404)

    return jsonify(menu.get_menu_item_data_with_id(db, id))

@app.route('/owners', methods=['GET'])
def get_all_owners_data():
    if request.method != 'GET': 
        return Response(status=404)
    return jsonify(user.get_all_owners_data(db))

@app.route('/customers', methods=['GET'])
def get_all_customers_data():
    if request.method != 'GET': 
        return Response(status=404)
    return jsonify(user.get_all_customers_data(db))    

@app.route('/waiters', methods=['GET'])
def get_all_waiters_data():
    if request.method != 'GET': 
        return Response(status=404)
    return jsonify(user.get_all_waiters_data(db))

@app.route('/cooks', methods=['GET'])
def get_all_cooks_data():
    if request.method != 'GET': 
        return Response(status=404)
    return jsonify(user.get_all_cooks_data(db))    

@app.route('/barmen', methods=['GET'])
def get_all_barmen_data():
    if request.method != 'GET': 
        return Response(status=404)
    return jsonify(user.get_all_barmen_data(db))   

@app.route('/foods', methods=['GET'])
def get_all_foods_data():
    if request.method != 'GET': 
        return Response(status=404)
    return jsonify(menu.get_all_foods_data(db)) 

@app.route('/drinks', methods=['GET'])
def get_all_drinks_data():
    if request.method != 'GET': 
        return Response(status=404)
    return jsonify(menu.get_all_drinks_data(db)) 

@app.route('/create-user', methods=['POST'])
def create_user():
    if request.method != 'POST': 
        return Response(status=404)

    # TODO : switch request.json[] to request.form.get() ?

    firstname = request.json["firstname"]
    lastname = request.json["lastname"]
    email = request.json["email"]
    phone = request.json["phone"]
    password = request.json["password"]
    type = request.json["type"]

    user.create_user(db, firstname, lastname, email, phone, password, type)
    auth.create_user_with_email_and_password(email, password)

    return Response(status=200)

@app.route('/sign-in', methods=['POST'])
def sign_in():
    if request.method != 'POST': 
        return Response(status=404)

    # TODO : switch request.json[] to request.form.get() ?

    email = request.json["email"]
    password = request.json["password"]

    auth.sign_in_with_email_and_password(email, password)

    return Response(status=200)

@app.route('/create-menu-item', methods=['POST'])
def create_menu_item():
    if request.method != 'POST': 
        return Response(status=404)

    # TODO : switch request.json[] to request.form.get() ?

    name = request.json["name"]
    description = request.json["description"]
    price = request.json["price"]
    type = request.json["type"]

    menu.create_menu_item(db, name, description, price, type)

    return Response(status=200)
 
@app.route('/delete-user-with-id', methods=['DELETE'])
def delete_user_with_id():
    if request.method != 'DELETE': 
        return Response(status=404)

    # TODO : switch request.json[] to request.form.get() ?

    id = request.json["id"]

    user.delete_user_with_id(db, id)

    return Response(status=200)

@app.route('/delete-menu-item-with-id', methods=['DELETE'])
def delete_menu_item_with_id():
    if request.method != 'DELETE': 
        return Response(status=404)

    # TODO : switch request.json[] to request.form.get() ?

    id = request.json["id"]

    menu.delete_menu_item_with_id(db, id)

    return Response(status=200)

@app.route('/update-menu-item-data-with-id', methods=['PUT'])
def update_menu_item_data_with_id():
    if request.method != 'PUT': 
        return Response(status=404)

    # TODO : switch request.json[] to request.form.get() ?

    id = request.json["id"]
    name = request.json["name"]
    description = request.json["description"]
    price = request.json["price"]
    type = request.json["type"]

    menu.update_menu_item_data_with_id(db, id, name, description, price, type)

    return Response(status=200)

@app.route('/update-user-data-with-id', methods=['PUT'])
def update_user_data_with_id():
    if request.method != 'PUT': 
        return Response(status=404)

    # TODO : switch request.json[] to request.form.get() ?

    id = request.json["id"]
    firstname = request.json["firstname"]
    lastname = request.json["lastname"]
    email = request.json["email"]
    phone = request.json["phone"]
    password = request.json["password"]
    type = request.json["type"]

    user.update_user_data_with_id(db, id, firstname, lastname, email, phone, password, type)

    return Response(status=200)
    
if __name__ == '__main__':
    app.run(debug=True)

# # NOTES # #
# set my own id :  db.child("user").child("myid").set(user)

# login = auth.sign_in_with_email_and_password(email, password)
# auth.send_email_verification(login['idToken'])

# auth.send_password_reset_email(email)