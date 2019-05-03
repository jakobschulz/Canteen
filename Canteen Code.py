
from bottle import run, route, view, get, post, request, static_file  
from itertools import count

class Food_Item:
    _ids = count(0)
    
    def __init__(self, name, price, stock):  #makes these variables for each item of food
        self.id = next(self._ids)
        self.name = name
        self.price = price
        self.stock = stock
        
items = [Food_Item("Sushi Roll", int(9), int(5)),
         Food_Item("Chips and Hot Dog", int(7), int(12)),
         Food_Item("Ham and Cheese Sandwich", int(6), int(4))]












run(host ='0.0.0.0', port = 8080, reloader = True, debug = True)