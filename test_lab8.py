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