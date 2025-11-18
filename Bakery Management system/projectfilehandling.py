import os

# ------------------------------------
# FILE NAMES
# ------------------------------------
USER_FILE = "users.txt"
MENU_FILE = "menu.txt"

# ------------------------------------
# LOAD USERS FROM FILE
# FORMAT: username,password,role,mobile
# ------------------------------------
def load_users():
    users = {}
    if not os.path.exists(USER_FILE):
        # Create admin by default
        with open(USER_FILE, "w") as f:
            f.write("admin,admin123,admin,9000000000\n")
    with open(USER_FILE, "r") as f:
        for line in f:
            if line.strip():
                u, p, r, m = line.strip().split(",")
                users[u] = {"password": p, "role": r, "mobile": m}
    return users

# ------------------------------------
# SAVE USERS TO FILE
# ------------------------------------
def save_users(users):
    with open(USER_FILE, "w") as f:
        for u, data in users.items():
            f.write(f"{u},{data['password']},{data['role']},{data['mobile']}\n")


# ------------------------------------
# LOAD MENU FROM FILE
# FORMAT: id,itemName
# ------------------------------------
def load_menu():
    menu = {}
    if not os.path.exists(MENU_FILE):
        with open(MENU_FILE, "w") as f:
            f.write("1,Chocolate Cake\n")
            f.write("2,Veg Puff\n")
            f.write("3,Paneer Roll\n")
            f.write("4,Cheese Sandwich\n")
    with open(MENU_FILE, "r") as f:
        for line in f:
            if line.strip():
                id_, item = line.strip().split(",")
                menu[int(id_)] = item
    return menu

# ------------------------------------
# SAVE MENU DATA
# ------------------------------------
def save_menu(menu):
    with open(MENU_FILE, "w") as f:
        for i, item in menu.items():
            f.write(f"{i},{item}\n")


# ------------------------------------
# MOBILE VALIDATION
# ------------------------------------
def validate_mobile(m):
    return len(m) == 10 and m.isdigit() and m.startswith("9")


# ------------------------------------
# LOGIN FUNCTION
# ------------------------------------
def login(users):
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in users and users[username]["password"] == password:
        print("\nLogin Successful!")
        return username
    else:
        print("\nInvalid username or password!")
        return None


# ------------------------------------
# MENU FUNCTIONS
# ------------------------------------
def view_menu(menu):
    print("\n--------- Bakery Menu ---------")
    for i, item in menu.items():
        print(f"{i}. {item}")

def search_item(menu):
    key = input("Enter name to search: ").lower()
    found = False
    for i, item in menu.items():
        if key in item.lower():
            print(f"Found → {i}. {item}")
            found = True
    if not found:
        print("No item matched.")

def add_item(menu):
    new_id = max(menu.keys()) + 1
    name = input("Enter new item name: ")
    menu[new_id] = name
    save_menu(menu)
    print("Item added.")

def delete_item(menu):
    view_menu(menu)
    try:
        item_id = int(input("Enter item ID to delete: "))
        if item_id in menu:
            del menu[item_id]
            save_menu(menu)
            print("Item deleted.")
        else:
            print("Invalid ID.")
    except:
        print("Invalid input.")


# ------------------------------------
# USER EDIT INFO
# ------------------------------------
def edit_user_info(username, users):
    new_mob = input("Enter new mobile (must start with 9 & be 10 digits): ")
    if validate_mobile(new_mob):
        users[username]["mobile"] = new_mob
        save_users(users)
        print("Mobile updated successfully!")
    else:
        print("Invalid mobile number!")


# ------------------------------------
# ADMIN PANEL
# ------------------------------------
def admin_panel(username, users, menu):
    while True:
        print("\n===== ADMIN MENU =====")
        print("1. View Menu")
        print("2. Search Item")
        print("3. Add Item")
        print("4. Delete Item")
        print("5. Edit Own Info")
        print("6. Logout")
        c = input("Enter choice: ")
        if c == "1":
            view_menu(menu)
        elif c == "2":
            search_item(menu)
        elif c == "3":
            add_item(menu)
        elif c == "4":
            delete_item(menu)
        elif c == "5":
            edit_user_info(username, users)
        elif c == "6":
            break
        else:
            print("Invalid choice!")


# ------------------------------------
# NORMAL USER PANEL
# ------------------------------------
def user_panel(username, users, menu):
    while True:
        print("\n===== USER MENU =====")
        print("1. View Menu")
        print("2. Search Item")
        print("3. Edit Own Info")
        print("4. Logout")
        c = input("Enter choice: ")
        if c == "1":
            view_menu(menu)
        elif c == "2":
            search_item(menu)
        elif c == "3":
            edit_user_info(username, users)
        elif c == "4":
            break
        else:
            print("Invalid choice!")


# ------------------------------------
# MAIN FUNCTION
# ------------------------------------
def main():
    users = load_users()
    menu = load_menu()
    print("===== Bakery Management System (File Version) =====")
    username = login(users)
    if not username:
        return
    role = users[username]["role"]
    if role == "admin":
        admin_panel(username, users, menu)
    else:
        user_panel(username, users, menu)


# RUN SYSTEM
main()
