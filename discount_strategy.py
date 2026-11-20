from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, price: float) -> float:
        pass

class NoDiscount(DiscountStrategy):
    def apply(self, total: float) -> float:
        return total

class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage: float):
        self.percentage = percentage #e.g. 10 = 10% discount

    def apply(self, total: float) -> float:
        return total * (1 - self.percentage / 100)

class BulkDiscount(DiscountStrategy):
    def __init__(self, threshold: float, discount_amount: float):
        self._threshold = threshold
        self._discount_amount = discount_amount

    def apply(self, total: float) -> float:
        if total >= self._threshold:
            return total - self._discount_amount
        return total