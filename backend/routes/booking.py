from math import ceil

from pyasn1.type.univ import Null

def get_booking_order(db, nb_persons=6, id_user="test_id"):
    """
    """
    nb_tables_needed = ceil(nb_persons / 4)

    tables = db.child("table").get()

    available_tables = 0
    available_tables_id = []

    for table in tables.each():        
        if table.val()['available'] == True:
            available_tables_id.append(table.key())
            available_tables+=1
    
    if (available_tables != 0):
        if (available_tables >= nb_tables_needed):            
            for i in range(0, nb_tables_needed):
                db.child("table").child(available_tables_id[i]).update({
                    "nbPlaces" : "4",
                    "available" : False,
                })   

                db.child("booking").push({
                    "userId" : id_user,
                    "arrivalTime" : "21-05-31-14:00",
                    "departureTime" : "21-05-31-14:00",
                    "nbPersons" : nb_persons,
                    "tableIds" : available_tables_id                    
                })
            return "Deux tables ont été réservé"
        else:
            return "Il n'y a pas assez de place"
    else:
        return "Nous sommes complet"