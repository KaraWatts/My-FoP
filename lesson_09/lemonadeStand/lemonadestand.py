class InvalidSalesItemError(Exception):
    pass

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
    
class LemonadeStand:
    
    def __init__(self, name):
        self._name = name
        self._currentDay = 0
        self._menuItemDictionary = {}
        self._salesForDayList = []

    def get_name(self):
        return self._name
    
    def get_currentDay(self):
        return self._currentDay
    
    def get_menu_item_dictionary(self):
        return self._menuItemDictionary
    
    def get_sales_for_the_day(self):
        return self._salesForDayList
    
    def add_menu_item(self, newMenuItem):
        newMenuItemDictionary = {
            newMenuItem._name: {
            '_wholesaleCost': newMenuItem._wholesaleCost,
            '_sellingPrice': newMenuItem._sellingPrice
            }
        }

        self._menuItemDictionary.update(newMenuItemDictionary)

    def enter_sales_for_today(self, salesOfDay):
            for key in salesOfDay:  
                if key not in self._menuItemDictionary:
                    raise InvalidSalesItemError("Item not on the menu")
            newSales = SalesForDay(self._currentDay, salesOfDay)
            self._salesForDayList.append(newSales)
            self._currentDay += 1


    def sales_of_menu_item_for_day(self, dayOfSales, menuItem):
        try:
            salesForDayObject = self._salesForDayList[dayOfSales]
            salesDictForDay = salesForDayObject.get_sales_dict()
            if menuItem in salesDictForDay:
                return salesDictForDay[menuItem]
            else:
                return 0
        except IndexError:
            return 'No information found for that day'
        
    
    def total_sales_for_menu_item(self, menuItem):
        totalSales = 0
        for index, value in enumerate(self._salesForDayList):
            salesOfDay = self.sales_of_menu_item_for_day(index, menuItem)
            if isinstance(salesOfDay, (int, float)):
                totalSales += salesOfDay
        return totalSales


    def total_profit_for_menu_item(self, menuItem):
            if menuItem not in self._menuItemDictionary:
                raise InvalidSalesItemError("Item not on the menu")
            else: 
                profitPerItem = self._menuItemDictionary[menuItem]["_sellingPrice"] - self._menuItemDictionary[menuItem]["_wholesaleCost"]
                totalItemProfit = profitPerItem * self.total_sales_for_menu_item(menuItem)
                return totalItemProfit


        


    def total_profit_for_stand(self):
        totalStandProfit = 0
        for key in self._menuItemDictionary:
            totalStandProfit += self.total_profit_for_menu_item(key)
        return totalStandProfit


    def __str__(self):
        return f"{self._name}, {self._currentDay}, {self._menuItemDictionary}, {self._salesForDayList}"


