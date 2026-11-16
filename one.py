#Inventory Management System

items= [] #list of dictionary:{"id","name", "quantity", "price"}
next_number = 101 #used to build IDs: I101 , I102 ,....
LOW_STOCK_LIMIT = 5


#create the next unique item ID (I101, I102, ....)
def generate_id():
    global next_number
    new_id = f"I{next_number}"
    next_number += 1
    return new_id 

#return the item dictionary with this ID or None if not found.
def find_item(item_id):
    for item in items:
        if item["id"] == item_id:
            return item
    return None
