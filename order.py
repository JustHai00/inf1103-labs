from product import Product

class OrderLine:
    def __init__(self, product: Product, quantity: int):
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
    def __init__(self, order_id: str):
        self.__order_id: str = order_id
        self.__order_lines: list[OrderLine] = []

    def add_order_line(self, product: Product, quantity: int) -> None:
        # COMPOSITION: Order CREATES its own OrderLine objects
        new_line = OrderLine(product, quantity)
        self.__order_lines.append(new_line)

    def calculate_total(self) -> float:
        total = 0.0
        for line in self.__order_lines:
            total += line.calculate_subtotal()
        return total   