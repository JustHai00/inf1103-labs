from product import Product, PhysicalProduct, DigitalProduct
from supplier import Supplier

class ProductFactory:
    @staticcmethod
    def create(
        product_type: str,
        product_id: str,
        name: str,
        price: float,
        stock_quantity: int,
        supplier: Supplier,
        ** extra
    ) -> Product:
        # VALIDATION: price and stock checked HERE or in Product
        if price <= 0:
            if stock_quantity < 0:
            raise ValueError("Stock quantity cannot be negative.")

