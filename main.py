import json
from product import Product
from inventory import Inventory

# File path
DATA_FILE = "inventory.json"

#  THIS IS THE MISSING FUNCTION — add it here
def save_inventory(inventory):
    try:
        products_data = [p.to_dict() for p in inventory.get_all_products()]
        with open(DATA_FILE, "w") as f:
            json.dump(products_data, f, indent=4)
        print(" Inventory saved successfully.")
    except Exception as e:
        print(f" Error saving file: {e}")

def load_inventory(inventory):
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            for item in data:
                product = Product(item["product_id"], item["name"], item["price"], item["stock"])
                inventory.add_product(product)
        print(" Inventory loaded successfully.")
    except FileNotFoundError:
        print("No existing inventory file found. Starting fresh.")
    except Exception as e:
        print(f" Error loading file: {e}")

def load_inventory(inventory: Inventory) -> None:
    """Load products from JSON file into Inventory object"""
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            for item in data:
                product = Product(
                    item["product_id"],
                    item["name"],
                    item["price"],
                    item["stock"]
                )
                inventory.add_product(product)
        print(" Inventory loaded successfully.")
    except FileNotFoundError:
        print(" No existing inventory file found. Starting fresh.")
    except Exception as e:
        print(f" Error loading file: {e}")   

def add_product_ui(inventory: Inventory) -> None:
    print("\n--- Add New Product ---")
    product_id = input("Enter Product ID: ").strip()
    name = input("Enter Product Name: ").strip()
    try:
        price = float(input("Enter Price: $"))
        stock = int(input("Enter Initial Stock: "))
        if price < 0 or stock < 0:
            print(" Price and stock cannot be negative!")
            return
    except ValueError:
        print(" Invalid number entered!")
        return

    product = Product(product_id, name, price, stock)
    if inventory.add_product(product):
        print(" Product added successfully!") 

def update_stock_ui(inventory: Inventory) -> None:
    print("\n--- Update Stock ---")
    product_id = input("Enter Product ID to update: ").strip()
    product = inventory.search_product(product_id)
    if not product:
        print(" Product not found!")
        return
    product.display_information()
    try:
        qty = int(input("Enter quantity to add (use negative to subtract): "))
    except ValueError:
        print(" Invalid number!")
        return
    if product.update_stock(qty):
        print(" Stock updated!")
        product.display_information() 

def search_product_ui(inventory: Inventory) -> None:
    print("\n--- Search Product ---")
    product_id = input("Enter Product ID to search: ").strip()
    product = inventory.search_product(product_id)
    if product:
        print("\n Product Found:")
        product.display_information()
    else:
        print(" Product not found.")  

def main():
    # Initialize inventory
    inventory = Inventory()
    load_inventory(inventory)

    while True:
        print("\n" + "="*40)
        print("       INVENTORY MANAGEMENT SYSTEM")
        print("="*40)
        print("1. Display All Products")
        print("2. Add New Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")
        print("="*40)

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            inventory.display_all()
        elif choice == "2":
            add_product_ui(inventory)
        elif choice == "3":
            update_stock_ui(inventory)
        elif choice == "4":
            search_product_ui(inventory)
        elif choice == "5":
            save_inventory(inventory)
        elif choice == "6":
            save_inventory(inventory)
            print(" Exiting program. Goodbye!")
            break
        else:
            print(" Invalid choice! Please enter 1-6.")

if __name__ == "__main__":
    main()