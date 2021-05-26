import pyrebase # pip install pyrebase4
import os
from dotenv import load_dotenv
from routes import user, menu


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


## Anthentification ##
# email = "alexzt@hotmail.fr"
# password = "mypassword"

# auth.sign_in_with_email_and_password(email, password)

# email = "alexzt2@hotmail.fr"
# password = "mypassword2"

# auth.create_user_with_email_and_password(email, password)

# use generated id
# db.child("user").push(user)

# set my own id

# db.child("user").child("myid").set(user)

# # # # # # MANAGEMENT # # # # # # #

# user.create_user(db, input("firstname : "), input("lastname : "), input("email : "), input("phone : "), input("password : "), input("type : "))

# print(user.get_user_data_with_id(db, input("id : "))

# print(user.get_all_users_data(db))

# print(user.get_all_waiters_data(db))

# print(user.get_all_customers_data(db))

# print(user.get_all_cooks_data(db))

# print(user.get_all_owners_data(db))

# print(user.get_all_barmen_data(db))

# menu.create_menu_item(db, "vodka", "encore une", 30, "drink")

# menu.create_menu_item(db, "twix", "ne se partage pas", 2, "food")

# print(menu.get_all_drinks_data(db))

# print(menu.get_all_foods_data(db))

# print(menu.get_menu_data(db))

# print(menu.get_menu_item_data_with_id(db, input("menu item id : ")))

# menu.delete_menu_item_with_id(db, input("menu item id : "))

# user.delete_user_with_id(db, input("user id : "))

menu.update_menu_item_data_with_id(
    db=db, 
    id=input("menu item id : "), 
    name=input("name  : "),
    description=input("description : "),
    price=input("price : "),
    type=input("type : "),
)

# user.update_user_data_from_id(
#     db=db, 
#     id=input("user id : "), 
#     firstname=input("firstname : "),
#     lastname=input("lastname : "), 
#     email=input("email : "),
#     phone=input("phone : "), 
#     password=input("password : "),
#     type=input("type : ")
# )