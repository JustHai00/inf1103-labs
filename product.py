from abc import ABC, abstractmethod
from supplier import Supplier  # import your new class

class Product(ABC):
    # ✅ UPDATED: added supplier parameter + type hint
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
