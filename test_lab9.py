from discount_strategy import NoDiscount, PercentageDiscount, BulkDiscount, StudentDiscount
from product_factory import ProductFactory
from supplier import Supplier
from inventory import Inventory
from order import Order
import csv


# ==============================================
# 1️⃣ HELPER — Safe User Input
# ==============================================
def get_positive_float(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("❌ Please enter a number greater than zero.")
                continue
            return value
        except ValueError:
            print("❌ Please enter a valid number, e.g. 12.50")


