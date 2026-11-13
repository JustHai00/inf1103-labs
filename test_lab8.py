from supplier import Supplier
from product import PhysicalProduct, DigitalProduct
from inventory import Inventory
from order import Order

def show_product_details(product):
    """Test LSP — works with ANY Product subclass"""
    product.display_information()
    print(f"  Fulfilment: {product.get_fulfilment_info()}")

# === TEST 1: Association ===
print("\n=== TEST 1: Association ===")
supplier = Supplier("S001", "Tech Supplies Co", "sales@techsupplies.com")
laptop = PhysicalProduct("P001", "Gaming Laptop", 1599.99, 10, 2.8, supplier)
ebook = DigitalProduct("D001", "Python Guide", 39.99, 100, 85, supplier)

print("Before deleting supplier:")
print(laptop.display_information())
print(f"Supplier: {laptop.get_supplier().get_name()}")

del supplier  # delete original reference
print("\nAfter deleting supplier variable:")
print(f"Laptop still knows supplier: {laptop.get_supplier().get_name()}")  # Still works!

# === TEST 2: Aggregation ===
print("\n=== TEST 2: Aggregation ===")
inv_a = Inventory()
inv_b = Inventory()

phone = PhysicalProduct("P002", "Smartphone", 799.99, 25, 0.18, 
                        Supplier("S002", "Mobile Distributors", "distro@mobile.com"))

inv_a.add_product(phone)
print(f"Inventory A before remove: {len(inv_a._Inventory__products)} products")

inv_a.remove_product("P002")
print(f"Inventory A after remove: {len(inv_a._Inventory__products)} products")

# Product still exists!
print(f"Product still works: {phone.display_information()}")

# Transfer to Inventory B
inv_b.add_product(phone)
print(f"Added to Inventory B: {inv_b.find_product('P002').get_name()}")
