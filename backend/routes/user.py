from pyasn1.type.univ import Null


def create_user(db, firstname, lastname, email, phone, password, type):
    """
    Used for create manually a user from the web interface
    """
    types = ["owner", "customer", "cook", "waiter", "barman"]

    if type in types:
        db.child("user").push(
            {
                "firstname" : firstname,
                "lastname" : lastname,
                "email" : email,
                "phone" : phone,
                "password" : password, 
                "type" : type
            }
        )

def get_all_users_data(db):
    return db.child("user").get().val()

def get_user_data_with_id(db, id):
    return db.child("user").child(id).get().val()

def update_user_data_with_id(db, id, firstname, lastname, email, phone, password, type):    
    types = ["owner", "customer", "cook", "waiter", "barman"]

    data = db.child("user").child(id).get().val()
    
    if firstname == "":
        firstname = data['firstname']

    if lastname == "":
        lastname = data['lastname']

    if email == "":
        email = data['email']

    if phone == "":
        phone = data['phone']

    if password == "":
        password = data['password']

    if type == "":
        type = data['type']

    if type in types:
        db.child("user").child(id).update(
            {
                "firstname" : firstname,
                "lastname" : lastname,
                "email" : email,
                "phone" : phone,
                "password" : password, 
                "type" : type
            }
        )
    else:
        print("ce role n'existe pas")
    
def get_all_cooks_data(db):
    users = db.child("user").get()
    data=[]

    for user in users.each():
        if user.val()['type'] == "cook":
            data.append(user.val())

    return data

def get_all_waiters_data(db):
    users = db.child("user").get()
    data=[]

    for user in users.each():
        if user.val()['type'] == "waiter":
            data.append(user.val())

    return data

def get_all_customers_data(db):
    users = db.child("user").get()
    data=[]

    for user in users.each():
        if user.val()['type'] == "customer":
            data.append(user.val())

    return data

def get_all_owners_data(db):
    users = db.child("user").get()
    data=[]

    for user in users.each():
        if user.val()['type'] == "owner":
            data.append(user.val())

    return data

def get_all_barmen_data(db):
    users = db.child("user").get()
    data=[]

    for user in users.each():
        if user.val()['type'] == "barman":
            data.append(user.val())

    return data    

def delete_user_with_id(db, id):
    # TODO : est-ce que l'utilisateur exsite ?
    db.child("user").child(id).remove()


# + : .order_by_child(string), .start_at(int), .end_at(int)