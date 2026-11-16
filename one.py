#Inventory Management System

item= [] #list of dictionary:{"id","name", "quantity", "price"}
next_number = 101 #used to build IDs: I101 , I102 ,....

#create the next unique item ID (I101, I102, ....)
def generate_id():
    global next_number
    next_id = f"I{next_number}"
    next_number += 1
    return new_id

