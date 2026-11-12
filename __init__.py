# In PhysicalProduct __init__:
def __init__(self, product_id: str, name: str, price: float, 
             stock: int, weight: float, supplier: Supplier):
    super().__init__(product_id, name, price, stock, supplier)
    self.__weight = weight