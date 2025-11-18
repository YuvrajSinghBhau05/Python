# -----------------------------------------------
#     BAKERY MANAGEMENT SYSTEM (PYTHON)
# -----------------------------------------------

# Sample users
users = {
    "admin": {
        "password": "admin123",
        "role": "admin",
        "mobile": "9000000000"
    },
    "john": {
        "password": "john123",
        "role": "user",
        "mobile": "9123456789"
    }
}

# Menu items dictionary
menu_items = {
    1: "Chocolate Cake",
    2: "Veg Puff",
    3: "Paneer Roll",
    4: "Cheese Sandwich"
}

# ------------------------------------------------
# MOBILE NUMBER VALIDATION
# ------------------------------------------------
def validate_mobile(mob):
    return len(mob) == 10 and mob.isdigit() and mob.startswith("9")


# ------------------------------------------------
# USER LOGIN
# ------------------------------------------------
def login():
    print("\n----- LOGIN -----")
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users and users[username]["password"] == password:
        print("Login successful!")
        return username
    else:
        print("Invalid login!")
        return None


# ------------------------------------------------
# MENU OPERATIONS (ADMIN)
# ------------------------------------------------
def add_item():
    item_id = max(menu_items.keys()) + 1
    name = input("Enter item name: ")
    menu_items[item_id] = name
    print("Item added successfully!")

def delete_item():
    view_menu()
    item_id = int(input("Enter item ID to delete: "))
    if item_id in menu_items:
        del menu_items[item_id]
        print("Item deleted.")
    else:
        print("Invalid ID")

def view_menu():
    print("\n------ BAKERY MENU ------")
    for i, item in menu_items.items():
        print(f"{i}. {item}")

def search_item():
    key = input("Enter item name to search: ").lower()
    found = False
    for i, item in menu_items.items():
        if key in item.lower():
            print(f"Found: {i}. {item}")
            found = True
    if not found:
        print("No matching items found.")


# ------------------------------------------------
# USER OPERATIONS (NORMAL USER)
# ------------------------------------------------
def edit_user_info(username):
    print("\n---- Edit Your Info ----")
    new_mobile = input("Enter new mobile (starts with 9 and 10 digits): ")

    if validate_mobile(new_mobile):
        users[username]["mobile"] = new_mobile
        print("Mobile updated successfully!")
    else:
        print("Invalid mobile number!")


# ------------------------------------------------
# ADMIN MENU
# ------------------------------------------------
def admin_panel(username):
    while True:
        print("\n===== ADMIN MENU =====")
        print("1. Add Menu Item")
        print("2. Delete Menu Item")
        print("3. View Menu")
        print("4. Search Item")
        print("5. Edit Own Info")
        print("6. Logout")

        choice = input("Enter choice: ")

        if choice == "1":
            add_item()
        elif choice == "2":
            delete_item()
        elif choice == "3":
            view_menu()
        elif choice == "4":
            search_item()
        elif choice == "5":
            edit_user_info(username)
        elif choice == "6":
            break
        else:
            print("Invalid choice")


# ------------------------------------------------
# USER MENU
# ------------------------------------------------
def user_panel(username):
    while True:
        print("\n===== USER MENU =====")
        print("1. View Menu")
        print("2. Search Item")
        print("3. Edit Own Info")
        print("4. Logout")

        choice = input("Enter choice: ")

        if choice == "1":
            view_menu()
        elif choice == "2":
            search_item()
        elif choice == "3":
            edit_user_info(username)
        elif choice == "4":
            break
        else:
            print("Invalid choice")


# ------------------------------------------------
# MAIN PROGRAM
# ------------------------------------------------
def main():
    print("===== Bakery Management System =====")

    username = login()
    if username is None:
        return

    # Check role
    role = users[username]["role"]

    if role == "admin":
        admin_panel(username)
    else:
        user_panel(username)


# Run Program
main()