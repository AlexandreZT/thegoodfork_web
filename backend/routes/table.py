def get_tables(db):
    """
    The number of table is limited to 10 (up to 40 customers)
    Display table list, if there is less than 10 tables, create them
    """
    tables = db.child("table").get().val()
    
    if (tables != None):
        tables = 0
    else:        
        current_number_of_tables = len(tables)

    while current_number_of_tables != 10:
        db.child("table").push(
                {
                    "nbPlaces" : "4",            
                    "available" : True
                }
            ) 
        current_number_of_tables+=1

    return db.child("table").get().val()