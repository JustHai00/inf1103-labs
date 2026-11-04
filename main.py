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

        if choice == "1":
            inv.display_all()

        elif choice == "2":
            print("\n--- Add New Product ---")
            print("Product type:")
            print("  1. Physical Product (has weight)")
            print("  2. Digital Product (has download size)")
            ptype = input("Enter choice (1 or 2): ")

            pid = input("Enter Product ID: ").strip()
            name = input("Enter Product Name: ").strip()
            try:
                price = float(input("Enter Price: $"))
                stock = int(input("Enter Initial Stock: "))
            except ValueError:
                print(" Invalid number — cancelled.")
                continue

            if ptype == "1":
                try:
                    weight = float(input("Enter Weight (kg): "))
                except ValueError:
                    print(" Invalid weight.")
                    continue
                product = PhysicalProduct(pid, name, price, stock, weight)
            elif ptype == "2":
                try:
                    size = float(input("Enter Download Size (MB): "))
                except ValueError:
                    print(" Invalid size.")
                    continue
                product = DigitalProduct(pid, name, price, stock, size)
            else:
                print(" Invalid type choice.")
                continue

            inv.add_product(product)
            print(f" Product added! {product.get_fulfilment_info()}")

        elif choice == "3":
            pid = input("\nEnter Product ID to update: ").strip()
            try:
                qty = int(input("Enter quantity (+ to add, - to remove): "))
            except ValueError:
                print(" Invalid number.")
                continue
            if inv.update_product_stock(pid, qty):
                print(" Stock updated.")
            else:
                print(" Product not found.")

        elif choice == "4":
            pid = input("\nEnter Product ID to search: ").strip()
            p = inv.search_product(pid)
            if p:
                print("\nFound:")
                print(p.display_information())
                if hasattr(p, 'calculate_shipping_cost'):
                    print(f"Shipping cost: ${p.calculate_shipping_cost():.2f}")
            else:
                print(" Product not found.")

        elif choice == "5":
            inv.save_to_json()

        elif choice == "6":
            print(" Goodbye!")
            break

        else:
            print(" Invalid choice — try 1-6.")

if __name__ == "__main__":
    main()
