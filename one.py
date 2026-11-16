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

# Return a non-negative whole number or None if invalid.
def parse_quantity(text):
    try:
        value = int(text)
    except ValueError:
        return None
    return value if value >= 0 else None

# Return a non-negative price  or None if invalid.
def parse_price(text):
    try:
        value = float(text)
    except ValueError:
        return None
    return value if value >= 0 else None
