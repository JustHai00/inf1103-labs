from inventory import Inventory
from product import PhysicalProduct, DigitalProduct

def main():
    inv = Inventory()
    inv.load_from_json()

    while True:
        print("\n" + "="*50)
        print("   INVENTORY MANAGEMENT SYSTEM — LAB 7")
        print("="*50)
        print("1. Display All Products")
        print("2. Add New Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")
        choice = input("\nEnter your choice (1-6): ")
