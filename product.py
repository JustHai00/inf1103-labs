class Product:
    def __init__(self, product_id: str, name: str, price: float, stock: int):
        # Private attributes (encapsulation)
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    # Getters (read-only access)
    def get_product_id(self) -> str:
        return self.__product_id

    def get_name(self) -> str:
        return self.__name

    def get_price(self) -> float:
        return self.__price

    def get_stock(self) -> int:
        return self.__stock

    # Method to update stock — add validation here
    def update_stock(self, quantity: int) -> bool:
        """Add quantity to stock; quantity can be negative to subtract. Return True if successful."""
        new_stock = self.__stock + quantity
        if new_stock >= 0:
            self.__stock = new_stock
            return True
        print(" Error: Stock cannot be negative!")
        return False

    def display_information(self) -> None:
        """Print product details neatly"""
        print(f"ID: {self.__product_id:8} | "
              f"Name: {self.__name:20} | "
              f"Price: ${self.__price:.2f} | "
              f"Stock: {self.__stock}")

    # For saving to JSON — convert object to dictionary
    def to_dict(self) -> dict:
        return {
            "product_id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock
        }