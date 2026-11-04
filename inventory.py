from product import Product

class Inventory:
    def __init__(self):
        self.__products: list[Product] = []

    def add_product(self, product: Product):
        self.__products.append(product)

    def search_product(self, product_id: str) -> Product | None:
        for p in self.__products:
            if p.get_product_id() == product_id:
                return p
        return None

    def display_all(self) -> None:
        """Show all products"""
        if not self.__products:
            print(" Inventory is empty.")
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