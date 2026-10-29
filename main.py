import json
from product import Product
from inventory import Inventory

# File path
DATA_FILE = "inventory.json"

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