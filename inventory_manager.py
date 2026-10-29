# ==========================================
# Inventory Management System — Week 5
# ==========================================

import json
DATA_FILE = "inventory.json"


def load_inventory():
    """Load from JSON file. Return empty dict if file missing or broken."""
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
        print(f" {DATA_FILE} found.")
        print(" Inventory loaded successfully.\n")
        return data
    
    except FileNotFoundError:
        print(f"ℹ {DATA_FILE} not found. Starting with empty inventory.\n")
        return {}
    
    except json.JSONDecodeError:
        print(f" {DATA_FILE} corrupted. Starting fresh.\n")
        return {}


def save_inventory(inventory):
    """Save inventory dict to JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(inventory, f, indent=4)
    print(f" Inventory saved successfully to {DATA_FILE}.\n")


def add_product(inventory, product_id, name, price, stock):
    """Add new product. Return True if added, False if ID exists."""
    if product_id in inventory:
        print(f" Product ID {product_id} already exists!\n")
        return False
    
    inventory[product_id] = {
        "name": name,
        "price": price,
        "stock": stock
    }
    print(" Product added successfully!\n")
    return True


def update_stock(inventory, product_id, new_stock):
    """Update stock quantity. Return True if found, False if not."""
    if product_id not in inventory:
        print(f" Product ID {product_id} not found!\n")
        return False
    
    inventory[product_id]["stock"] = new_stock
    print(" Stock updated successfully!\n")
    return True


def search_product(inventory, product_id):
    """Search by ID. Return product dict or None."""
    if product_id not in inventory:
        print(" Product not found.\n")
        return None
    
    p = inventory[product_id]
    print(f" Product Found")
    print(f"ID: {product_id} | Name: {p['name']} | Price: ${p['price']:.2f} | Stock: {p['stock']}\n")
    return p


def display_all(inventory):
    """Show all products in inventory."""
    if not inventory:
        print(" Inventory is empty.\n")
        return
    
    print(" Current Inventory")
    print("-" * 55)
    for pid, p in inventory.items():
        print(f"ID: {pid:6} | Name: {p['name']:15} | Price: ${p['price']:7.2f} | Stock: {p['stock']:3}")
    print("-" * 55 + "\n")


# ==========================================
# MAIN MENU SYSTEM
# ==========================================

def main():
    print("=" * 50)
    print("       INVENTORY MANAGEMENT SYSTEM")
    print("=" * 50 + "\n")
    
    # Load existing data
    inventory = load_inventory()

    while True:
        print("----------- MENU -----------")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")
        
        choice = input("Enter option: ").strip()

        if choice == "1":
            display_all(inventory)

        elif choice == "2":
            print("\n Add New Product")
            pid = input("Product ID: ").strip().upper()
            name = input("Product Name: ").strip()
            
            try:
                price = float(input("Price: ").strip())
                stock = int(input("Stock Quantity: ").strip())
            except ValueError:
                print(" Invalid number! Price and stock must be numbers.\n")
                continue
            
            add_product(inventory, pid, name, price, stock)

        elif choice == "3":
            print("\n Update Stock")
            pid = input("Enter Product ID: ").strip().upper()
            
            if pid not in inventory:
                print(f" Product ID {pid} not found!\n")
                continue
            
            p = inventory[pid]
            print(f"Product Found: {p['name']} | Current Stock: {p['stock']}")
            
            try:
                new_stock = int(input("New Stock Quantity: ").strip())
            except ValueError:
                print(" Please enter a valid whole number.\n")
                continue
            
            update_stock(inventory, pid, new_stock)

        elif choice == "4":
            print("\n Search Product")
            pid = input("Enter Product ID: ").strip().upper()
            search_product(inventory, pid)

        elif choice == "5":
            print("\n Saving inventory...")
            save_inventory(inventory)

        elif choice == "6":
            print("\n Saving inventory before exit...")
            save_inventory(inventory)
            print("Thank you for using Inventory Management System.")
            print("Program terminated.")
            break

        else:
            print(" Invalid option! Please enter 1–6.\n")


if __name__ == "__main__":
    main()