# Shopping List App (Python)

A simple console-based Shopping List application built in Python.  
It allows users to add, remove, and view items from their list — all while logging actions in real-time using Python’s `logging` module.

---

## Features

- Add new items to your shopping list  
- Remove existing items  
- View all current items  
- Logging system for tracking actions  
- Clean modular code using separate files (`main.py`, `list_manager.py`)  
- Beginner-friendly structure — great for learning modular programming

---

## Project Structure

shopping_list/
├── main.py # Runs the program and handles user input
└── list_manager.py # Contains add/remove functions and logging setup

---

## How It Works

1. The program starts by showing a menu:
(A)Add, (R)Remove, (V)View, (Q)Quit:
2. Type `A` to add an item, `R` to remove one, or `V` to view your list.  
3. All actions are recorded with timestamps in the console via the logging system.

Example log:
2025-10-15 10:22:30 - INFO - Added 'Milk' successfully!

---

## Requirements

- Python 3.x installed  
- No extra libraries are needed (uses only Python built-ins)

---

## How to Run

Clone the repository and run it with Python:

```bash
git clone https://github.com/sayikimm/shopping-list-app.git
cd shopping-list-app
python main.py
```

---

## Concepts Practiced

- Modular programming
- Logging and debugging
- Type hints for readability
- Clean user input handling
- Refactoring simple scripts into structured programs
  

## Future Improvements
- Save and load the shopping list from a file (shopping_list.json)
- Add categories (groceries, electronics, etc.)
- Create a simple GUI or web version

## Author
- Mikiyas Sisay
- https://github.com/sayikimm
