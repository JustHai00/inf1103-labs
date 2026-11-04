from abc import ABC, abstractmethod

# --- Interface: CanBeShipped ---
class CanBeShipped(ABC):
    @abstractmethod
    def calculate_shipping_cost(self) -> float:
        """Return shipping cost — implemented by PhysicalProduct"""
        pass
    
# --- Abstract Product Class ---
class Product(ABC):
    def __init__(self, product_id: str, name: str, price: float, stock: int):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock