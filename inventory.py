from product import Product

class Inventory:
    def __init__(self):
        self.__products: list[Product] = []  # ✅ Type hint

    def add_product(self, product: Product) -> None:
        self.__products.append(product)

    def remove_product(self, product_id: str) -> bool:
        for i, p in enumerate(self.__products):
            if p.get_product_id() == product_id:
                del self.__products[i]
                return True
        return False

    def find_product(self, product_id: str) -> Product | None:
        for p in self.__products:
            if p.get_product_id() == product_id:
                return p
        return None

    def display_all(self) -> None:
        if not self.__products:
            print("No products in inventory.")
            return
        print("\n=== INVENTORY ===")
        for p in self.__products:
            print(p.display_information())
            print(f"  Supplier: {p.get_supplier().get_name()}")
