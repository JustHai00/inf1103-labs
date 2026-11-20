from discount_strategy import NoDiscount, PercentageDiscount, BulkDiscount, StudentDiscount
from product_factory import ProductFactory
from supplier import Supplier
from inventory import Inventory
from order import Order
import csv


# ==============================================
#  HELPER — Safe User Input
# ==============================================
def get_positive_float(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print(" Please enter a number greater than zero.")
                continue
            return value
        except ValueError:
            print(" Please enter a valid number, e.g. 12.50")

# ==============================================
#  LOAD — Read CSV File Safely
# ==============================================
def load_products_safely(file_path: str, inventory: Inventory, supplier: Supplier) -> None:
    loaded_count = 0
    
    try:
        with open(file_path, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            
            for row_num, row in enumerate(reader, start=2):
                try:
                    product = ProductFactory.create(
                        product_type=row["product_type"],
                        product_id=row["product_id"],
                        name=row["name"],
                        price=float(row["price"]),
                        stock_quantity=int(row["stock_quantity"]),
                        supplier=supplier,
                        weight=float(row.get("weight", 0)) if row.get("weight") else None,
                        download_size=float(row.get("download_size", 0)) if row.get("download_size") else None
                    )
                    inventory.add_product(product)
                    loaded_count += 1
                    
                except ValueError as e:
                    print(f" Skipping row {row_num}: {e}")
    
    except FileNotFoundError:
        print(f" Error: Could not find file '{file_path}'")
    
    else:
        print(f" Successfully loaded {loaded_count} products!")
    
    finally:
        print(" Load operation completed.")

# ==============================================
#  TEST — Run Everything
# ==============================================
if __name__ == "__main__":
    print("===== TEST 1: User Input =====")
    price = get_positive_float("Enter price: $")
    print(f"You entered: ${price}")

    print("\n===== TEST 2: Load CSV =====")
    supplier = Supplier("S001", "Tech Supplies", "sales@tech.com")
    inv = Inventory()
    load_products_safely("products.csv", inv, supplier)
