class MenuItem:

    def __init__(self, name, wholesaleCost, sellingPrice):
        self._name = name
        self._wholesaleCost = wholesaleCost
        self._sellingPrice = sellingPrice

    def get_name(self):
        return self._name
    
    def get_wholesale_cost(self):
        return self._wholesaleCost
    
    def get_selling_price(self):
        return self._sellingPrice
    
    def __str__(self):
        return f"{self._name}, {self._wholesaleCost}, {self._sellingPrice}"