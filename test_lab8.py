from supplier import Supplier
from product import PhysicalProduct, DigitalProduct
from inventory import Inventory
from order import Order

def show_product_details(product):
    """Test LSP — works with ANY Product subclass"""
    product.display_information()
    print(f"  Fulfilment: {product.get_fulfilment_info()}")