import json

from product import DigitalProduct, LegacyProduct, PhysicalProduct, Product

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

    def display_all(self):
        if not self.__products:
            print("No products in inventory.")
            return
        print("\n" + "="*60)
        print("INVENTORY LIST")
        print("="*60)
        for p in self.__products:
            print(p.display_information())
            # Show shipping cost if applicable
            if hasattr(p, 'calculate_shipping_cost'):
                print(f"  → Shipping cost: ${p.calculate_shipping_cost():.2f}")
        print("="*60 + "\n")

    def update_product_stock(self, product_id: str, quantity: int) -> bool:
        p = self.search_product(product_id)
        if p:
            return p.update_stock(quantity)
        return False

    # --- JSON Save/Load with type detection ---
    def save_to_json(self, filename: str = "inventory.json"):
        data = [p.to_dict() for p in self.__products]
        with open(filename, "w") as f:
            json.dump(data, f, indent=2)
        print(" Inventory saved successfully.")

    def load_from_json(self, filename: str = "inventory.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            print(" No existing inventory file found. Starting fresh.")
            return

        self.__products.clear()
        for item in data:
            product_type = item.get("type")
            if product_type == "physical":
                product = PhysicalProduct(
                    item["product_id"], item["name"],
                    item["price"], item["stock"], item["weight"]
                )
            elif product_type == "digital":
                product = DigitalProduct(
                    item["product_id"], item["name"],
                    item["price"], item["stock"], item["download_size"]
                )
            elif product_type == "legacy" or product_type is None:
                product = LegacyProduct(
                    item["product_id"], item["name"],
                    item["price"], item["stock"]
                )
            else:
                continue  # skip unknown types
            self.__products.append(product)
        print(f" Inventory loaded successfully — {len(self.__products)} products.")