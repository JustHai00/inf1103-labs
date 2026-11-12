class Supplier:
    def __init__(self, supplier_id: str, name: str, contact_email: str):
        self.__supplier_id = supplier_id
        self.__name = name
        self.__contact_email = contact_email

    def get_supplier_id(self) -> str:
        return self.__supplier_id