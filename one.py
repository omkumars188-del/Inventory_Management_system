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

# Display a list of items in a neat table.
def print_table(rows):
    print("-" * 54)
    print(f"{'ID':<8}{'Name':<20}{'Quantity':>10}{'Price':>14}")
    print("-" * 54)
    for item in rows:
        print(f"{item['id']:<8}{item['name']:<20}{item['quantity']:>10}{item['price']:>14g}")
    print("-" * 54)

    # CRUD + feature

def add_item():
    name = input("Name: ").strip()
    if not name:
        print("Error: Name cannot be empty. Item not added.")
        return

    qty = parse_quantity(input("Quantity: "))
    if qty is None:
        print("Invalid quantity. Quantity must be a non-negative whole number. Item not added.")
        return

    price = parse_price(input("Price: "))
    if price is None:
        print("Invalid price. Price must be a non-negative number. Item not added.")
        return

    item = {"id": generate_id(), "name": name, "quantity": qty, "price": price}
    items.append(item)
    print("Item added.")
    print(f"ID: {item['id']} | {name} | Qty: {qty} | Price: {price:g}")

    if qty < LOW_STOCK_LIMIT:
        print(f"Low stock alert: {name} ({qty})")


def view_items():
    if not items:
        print("No items in inventory.")
        return
    print_table(items)


def update_item():
    item_id = input("Enter item ID to update: ").strip().upper()
    item = find_item(item_id)
    if item is None:
        print(f"Item ID {item_id} not found.")
        return

    new_qty = input(f"New quantity (press Enter to keep {item['quantity']}): ").strip()
    if new_qty:
        qty = parse_quantity(new_qty)
        if qty is None:
            print("Invalid quantity. Update cancelled.")
            return
        item["quantity"] = qty

    new_price = input(f"New price (press Enter to keep {item['price']:g}): ").strip()
    if new_price:
        price = parse_price(new_price)
        if price is None:
            print("Invalid price. Update cancelled.")
            return
        item["price"] = price

    print("Item updated.")
    print_table([item])


def search_item():
    keyword = input("Enter ID or name to search: ").strip().lower()
    results = [
        item for item in items
        if keyword in item["id"].lower() or keyword in item["name"].lower()
    ]
    if results:
        print_table(results)
    else:
        print("No matching items found.")


def delete_item():
    item_id = input("Enter item ID to delete: ").strip().upper()
    item = find_item(item_id)
    if item is None:
        print(f"Item ID {item_id} not found.")
        return

    items.remove(item)
    print(f"Item '{item['name']}' deleted. Items left: {len(items)}")


def total_stock_value():
    total = sum(item["quantity"] * item["price"] for item in items)
    print(f"Total stock value: {total:g}")


def low_stock_report():
    low = [item for item in items if item["quantity"] < LOW_STOCK_LIMIT]
    if not low:
        print("No low-stock items.")
        return
    print(f"Low-stock items (quantity below {LOW_STOCK_LIMIT}):")
    print_table(low)

#    Main menu


MENU = """
 Inventory Management System 
1. Add item
2. View items
3. Update item
4. Delete item
5. Total stock value
6. Low-stock report
7. Search item
0. Exit
"""


def main():
    while True:
        print(MENU)
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_item()
        elif choice == "2":
            view_items()
        elif choice == "3":
            update_item()
        elif choice == "4":
            delete_item()
        elif choice == "5":
            total_stock_value()
        elif choice == "6":
            low_stock_report()
        elif choice == "7":
            search_item()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()