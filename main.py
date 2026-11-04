from inventory import Inventory
from product import PhysicalProduct, DigitalProduct

def main():
    inv = Inventory()
    inv.load_from_json()
