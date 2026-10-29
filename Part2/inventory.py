from product import Product

class Inventory:
    def __init__(self):
        self.__products = []  # Stores Product objects

    def add_product(self, product: Product) -> bool:
        """Add a Product object; prevent duplicate IDs"""
        if self.search_product(product.get_product_id()):
            print(" Product with this ID already exists!")
            return False
        self.__products.append(product)
        return True

    def search_product(self, product_id: str) -> Product | None:
        """Return Product object if found, else None"""
        for product in self.__products:
            if product.get_product_id() == product_id:
                return product
        return None

    def search_product(self, product_id: str) -> Product | None:
        """Return Product object if found, else None"""
        for product in self.__products:
            if product.get_product_id() == product_id:
                return product
        return None

    def display_all(self) -> None:
        """Show all products"""
        if not self.__products:
            print("📭 Inventory is empty.")
            return
        print("\n" + "="*65)
        print(" " * 15 + "INVENTORY LIST")
        print("="*65)
        for product in self.__products:
            product.display_information()
        print("="*65 + "\n")

    def get_all_products(self) -> list[Product]:
        """Return list of products for saving to file"""
        return self.__products