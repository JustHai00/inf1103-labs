from product import Product
from discount_strategy import DiscountStrategy, NoDiscount


class OrderLine:
    def __init__(self, product: Product, quantity: int):
        # ✅ Validation — quantity must be positive
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        self.__product = product
        self.__quantity = quantity

    def calculate_subtotal(self) -> float:
        return self.__product.get_price() * self.__quantity

    def get_product(self) -> Product:
        return self.__product

    def get_quantity(self) -> int:
        return self.__quantity

    def display(self) -> str:
        return f"{self.__product.get_name()} × {self.__quantity} = ${self.calculate_subtotal():.2f}"


class Order:
    def __init__(self, order_id: str, discount_strategy: DiscountStrategy = None):
        self.__order_id: str = order_id
        self.__order_lines: list[OrderLine] = []
        # Use NoDiscount if none provided
        self.__discount = discount_strategy if discount_strategy else NoDiscount()

    def set_discount(self, discount_strategy: DiscountStrategy) -> None:
        self.__discount = discount_strategy

    def add_order_line(self, product: Product, quantity: int) -> None:
        new_line = OrderLine(product, quantity)
        self.__order_lines.append(new_line)

    def calculate_total(self) -> float:
        total = sum(line.calculate_subtotal() for line in self.__order_lines)
        return self.__discount.apply(total)

    def display_order(self) -> None:
        print(f"\n=== Order: {self.__order_id} ===")
        for line in self.__order_lines:
            print(f"  {line.display()}")
        print(f"  TOTAL: ${self.calculate_total():.2f}")
