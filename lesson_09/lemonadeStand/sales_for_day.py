class SalesForDay:

    def __init__(self, numberOfDays, salesDictionary):
        self._numberOfDays = numberOfDays
        self._salesDictionary = salesDictionary

    def get_day(self):
        return self._numberOfDays
    
    def get_sales_dict(self):
        return self._salesDictionary
    
    def __str__(self):
        return f"{self._numberOfDays}, {self._salesDictionary}"