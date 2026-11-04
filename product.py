from abc import ABC, abstractmethod

# --- Interface: CanBeShipped ---
class CanBeShipped(ABC):
    @abstractmethod
    def calculate_shipping_cost(self) -> float:
        """Return shipping cost — implemented by PhysicalProduct"""
        pass