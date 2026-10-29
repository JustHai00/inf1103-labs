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