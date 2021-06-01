def create_menu_item(db, name, description, price, type):
    """
    Used when adding menu item from the web interface
    """
    if type == "drink" or type == "food" :
        db.child("menu").push(
            {
                "name" : name,
                "description" : description,
                "price" : price, 
                "type" : type
            }
        ) 

def get_menu_data(db):
    return db.child("menu").get().val()

def get_menu_item_data_with_id(db, id):
    return db.child("menu").child(id).get().val()

def get_all_drinks_data(db):
    menu = db.child("menu").get()
    drinks={}

    for item in menu.each():
        if item.val()['type'] == "drink":
            drinks.update({item.key() : item.val()})

    return drinks

def get_all_foods_data(db):
    menu = db.child("menu").get()
    foods={}

    for item in menu.each():
        if item.val()['type'] == "food":
            foods.update({item.key() : item.val()})

    return foods

def delete_menu_item_with_id(db, id):
    db.child("menu").child(id).remove()

def update_menu_item_data_with_id(db, id, name, description, price, type):
    types = ["food", "drink"]

    data = db.child("menu").child(id).get().val()
    
    if name == "":
        name = data['name']

    if description == "":
        description = data['description']

    if price == "":
        price = data['price']

    if type == "":
        type = data['type']

    if type in types:
        db.child("menu").child(id).update(
            {
                "name" : name,
                "description" : description,
                "price" : price,
                "type" : type,
            }
        )
    else:
        print("ce rôle n'existe pas")


# + : .order_by_child(string), .start_at(int), .end_at(int)