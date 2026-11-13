from abc import ABC, abstractmethod
from supplier import Supplier  # import your new class

class Product(ABC):
    #  UPDATED: added supplier parameter + type hint
    def __init__(self, product_id: str, name: str, price: float, 
                 stock: int, supplier: Supplier):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock
        self.__supplier = supplier  # Association — stores reference only

    # Getters
    def get_product_id(self) -> str: return self.__product_id
    def get_name(self) -> str: return self.__name
    def get_price(self) -> float: return self.__price
    def get_stock(self) -> int: return self.__stock
    def get_supplier(self) -> Supplier: return self.__supplier

    def update_stock(self, quantity: int) -> bool:
        if isinstance(quantity, int):
            self.__stock += quantity
            return True
        return False

    @abstractmethod
    def get_fulfilment_info(self) -> str: pass

    @abstractmethod
    def display_information(self) -> str: pass

    @abstractmethod
    def to_dict(self) -> dict: pass


class PhysicalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float, stock: int,
                 weight: float, supplier: Supplier):
        super().__init__(product_id, name, price, stock, supplier)
        self.__weight = weight

    def get_weight(self) -> float:
        return self.__weight

    def get_fulfilment_info(self) -> str:
        return f"Physical item weighing {self.__weight} kg"

    def display_information(self) -> str:
        return (f"Physical Product: {self.get_name()} "
                f"(ID: {self.get_product_id()}) | Price: ${self.get_price():.2f} "
                f"| Stock: {self.get_stock()} | Weight: {self.__weight} kg")

    def to_dict(self) -> dict:
        return {
            "type": "physical",
            "product_id": self.get_product_id(),
            "name": self.get_name(),
            "price": self.get_price(),
            "stock": self.get_stock(),
            "weight": self.__weight,
        }


class DigitalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float, stock: int,
                 download_size: float, supplier: Supplier):
        super().__init__(product_id, name, price, stock, supplier)
        self.__download_size = download_size

    def get_download_size(self) -> float:
        return self.__download_size

    def get_fulfilment_info(self) -> str:
        return f"Digital download ({self.__download_size} MB)"

    def display_information(self) -> str:
        return (f"Digital Product: {self.get_name()} "
                f"(ID: {self.get_product_id()}) | Price: ${self.get_price():.2f} "
                f"| Stock: {self.get_stock()} | Download size: {self.__download_size} MB")

    def to_dict(self) -> dict:
        return {
            "type": "digital",
            "product_id": self.get_product_id(),
            "name": self.get_name(),
            "price": self.get_price(),
            "stock": self.get_stock(),
            "download_size": self.__download_size,
        }
