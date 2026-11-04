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

# --- Physical Product ---
class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id: str, name: str, price: float, stock: int, weight: float):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight  # in kg

    def get_weight(self): return self.__weight

    def get_fulfilment_info(self) -> str:
        return f"Requires physical shipping. Weight: {self.__weight} kg"

    def display_information(self) -> str:
        base = self._base_info()
        return f"{base} | Weight: {self.__weight} kg — {self.get_fulfilment_info()}"

    def calculate_shipping_cost(self) -> float:
        # Simple rule: $3.50 per kg
        return round(self.__weight * 3.50, 2)

    def to_dict(self) -> dict:
        return {
            "type": "physical",
            "product_id": self.get_product_id(),
            "name": self.get_name(),
            "price": self.get_price(),
            "stock": self.get_stock(),
            "weight": self.__weight
        }

# --- Digital Product ---
class DigitalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float, stock: int, download_size: float):
        super().__init__(product_id, name, price, stock)
        self.__download_size = download_size  # in MB

    def get_download_size(self): return self.__download_size

    def get_fulfilment_info(self) -> str:
        return f"Delivered digitally. Download size: {self.__download_size} MB"

    def display_information(self) -> str:
        base = self._base_info()
        return f"{base} | Download: {self.__download_size} MB — {self.get_fulfilment_info()}"

    def to_dict(self) -> dict:
        return {
            "type": "digital",
            "product_id": self.get_product_id(),
            "name": self.get_name(),
            "price": self.get_price(),
            "stock": self.get_stock(),
            "download_size": self.__download_size
        }


class LegacyProduct(Product):
    """Product loaded from an inventory record without a product type."""

    def get_fulfilment_info(self) -> str:
        return "Fulfilment details unavailable for this legacy product."

    def display_information(self) -> str:
        return f"{self._base_info()} | {self.get_fulfilment_info()}"

    def to_dict(self) -> dict:
        return {
            "type": "legacy",
            "product_id": self.get_product_id(),
            "name": self.get_name(),
            "price": self.get_price(),
            "stock": self.get_stock()
        }