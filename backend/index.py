import pyrebase # pip install pyrebase4
from routes import user, menu


firebaseConfig = {
    'apiKey': "AIzaSyBxbqpIMduyrYePBbughqIRsGZPIUhhrZQ",
    'authDomain': "proj-2020-21.firebaseapp.com",
    'databaseURL': "https://proj-2020-21-default-rtdb.europe-west1.firebasedatabase.app",
    'projectId': "proj-2020-21",
    'storageBucket': "proj-2020-21.appspot.com",
    'messagingSenderId': "49533013005",
    'appId': "1:49533013005:web:f32396f5fc17da6a285944", # "1:49533013005:web:55c8af614a4f7357285944"
    'measurementId': "G-G9LF4Z20G6" # "G-BNHESS4RSD"
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