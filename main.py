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

