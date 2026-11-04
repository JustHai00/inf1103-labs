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

    # Getters
    def get_product_id(self): return self.__product_id
    def get_name(self): return self.__name
    def get_price(self): return self.__price
    def get_stock(self): return self.__stock

    # Setters
    def update_stock(self, quantity: int) -> bool:
        if isinstance(quantity, int):
            self.__stock += quantity
            return True
        return False

    @abstractmethod
    def get_fulfilment_info(self) -> str:
        """Return delivery/shipping message — MUST implement in subclasses"""
        pass

    @abstractmethod
    def display_information(self) -> str:
        """Show product details — override in subclasses"""
        pass

    @abstractmethod
    def to_dict(self) -> dict:
        """Serialize including type — for JSON saving"""
        pass

    # Common helper for subclasses to reuse
    def _base_info(self) -> str:
        return (f"ID: {self.__product_id} | Name: {self.__name} | "
                f"Price: ${self.__price:.2f} | Stock: {self.__stock}")