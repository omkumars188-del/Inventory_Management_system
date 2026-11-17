# Project Summary: Inventory Management System

**Language:** Python 3

**Concepts:** Lists, Dictionaries, Functions, Loops, Conditions, Input Validation, Exception Handling

**Code file:** `inventory.py`

---

## 1. Project Overview

This project is a console-based inventory management system. It keeps a list of items in memory, and each item has an ID, a name, a quantity and a price. A menu lets the user add, view, update, delete and search items, see the total stock value, and see a low-stock report. IDs are made automatically (`I101`, `I102`, ...). An item is called low stock when its quantity is below 5. The menu keeps running until the user chooses `0. Exit`.

## 2. What I Have Done

- Stored the items in a list of dictionaries. Each dictionary has the keys `id`, `name`, `quantity` and `price`.
- Made a function `generate_id()` that creates the next unique ID (`I101`, `I102`, ...) using a global counter `next_number`.
- Made a function `find_item()` that uses a **`for` loop** to find an item by its ID, and returns `None` if it is not found.
- Made two functions, `parse_quantity()` and `parse_price()`. They use `try/except` to accept only a non-negative whole number for quantity and a non-negative number for price.
- Made a function `print_table()` that shows items in a neat table using f-string alignment.
- Made a separate function for each menu option: `add_item()`, `view_items()`, `update_item()`, `delete_item()`, `total_stock_value()`, `low_stock_report()` and `search_item()`.
- Checked that the name is not empty when adding an item.
- Showed a low stock alert when an added item has a quantity below `LOW_STOCK_LIMIT` (5).
- In the update option, let the user press Enter to keep the old quantity or price.
- Made the search work on both ID and name. It is not case sensitive and also finds part of a word, using a list comprehension.
- Used `sum()` with a generator expression to calculate the total stock value (quantity × price for all items).
- Used a **`while True` loop** with `if`, `elif` and `else` for the main menu, and `break` to exit.
- Added a message for wrong menu choices: `Invalid option. Please try again.`
- Used `if __name__ == "__main__":` so the program starts only when the file is run directly.
- Tested the program with the test cases given below.

## 3. Test Cases and Screenshots

### Test Case 1:
<img width="1919" height="1149" alt="Screenshot from 2026-11-17 09-08-26" src="https://github.com/user-attachments/assets/9d7dfe4b-9d53-45b2-b087-35bb40337cea" />



### Test Case 2:



### Test Case 3:



### Test Case 4:



## 4. Hardships Faced and How I Overcame Them

| Hardship | How I Overcame It |
|---|---|
| **Program crashed on wrong quantity or price.** Typing `abc` gave a `ValueError`. | I made `parse_quantity()` and `parse_price()` with `try/except`. They return `None` for bad input, and the calling function shows an error message. |
| **Negative numbers were accepted.** A quantity or price below 0 made no sense. | I added a check `value >= 0` in both parse functions, so a negative value is treated as invalid. |
| **Decimal quantity was accepted at first.** A quantity like `2.5` does not make sense for items. | I used `int()` for quantity and `float()` for price, so `2.5` is rejected as a quantity but accepted as a price. |
| **Empty item name.** An item with a blank name could be added. | I used `.strip()` and checked `if not name` before anything else, so the item is not added. |
| **IDs repeated after deleting an item.** If IDs were made from the list length, a new item could get the same ID as an older one. | I used a separate counter `next_number` that only goes up, so IDs are never reused. |
| **Changing a global variable.** Python gave an error when I changed `next_number` inside a function. | I declared it with the `global` keyword inside `generate_id()`. |
| **Wrong case in item IDs.** Typing `i101` did not match `I101`. | I used `.strip().upper()` on the ID before searching. |
| **Update changed only half the values.** If the price was wrong, the quantity was already changed. | I check each value before it is saved, and cancel the update with a message when it is invalid. |
| **Keeping the old value when updating.** I wanted the user to change only one field. | I let the user press Enter on a field to keep the old value, by checking `if new_qty:` before updating. |
| **Table columns were not lined up.** Long names and numbers made the output messy. | I used f-string widths like `:<20` and `:>10`, and `:g` for prices, so columns line up and `50.0` prints as `50`. |
| **Search found nothing for small letters.** Searching `laptop` did not find `Laptop`. | I changed both the keyword and the item values to lower case before comparing. |
| **Empty inventory caused confusing output.** View, report and total were shown with no items. | I added a check `if not items` and print `No items in inventory.` instead of an empty table. |

## 5. What I Learned

- How to store records in a list of dictionaries and loop through them.
- How to build a menu-driven program using a `while` loop and functions.
- How to divide a program into small functions that each do one job.
- How to check user input with `try/except` and return `None` for bad values.
- How to use list comprehensions and `sum()` to filter and total data.
- How to format output neatly using f-strings.
- How to use `global` variables, and when they are needed.
- How to test a program against different cases and find the reason for a difference in output.

## 6. How to Run

```bash
python inventory.py
```

No external libraries are needed. Items are kept only in memory, so they are lost when the program stops.

## 7. Files in This Project

```
Inventory-Management-System/
├── inventory.py   # main program
├── images/        # screenshots of the test cases
├── README.md      # project description
└── Summary.md     # this summary
```
