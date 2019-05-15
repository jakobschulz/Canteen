from bottle import run, route, view, get, post, request, static_file  
from itertools import count

class Food_Item:
    _ids = count(0)
    
    def __init__(self, name, price, stock):  #makes these variables for each item of food
        self.id = next(self._ids)
        self.name = name
        self.image = image
        self.price = price
        self.stock = stock
        
#this is my class containg each of my food items.
items = [Food_Item("Sushi Roll","sushi.jpg" ,int(9), int(5)), 
         Food_Item("Chips and Hot Dog","Hot dogs.jpg" , int(7), int(12)),
         Food_Item("Ham and Cheese Sandwich", "",int(6), int(4))] 


#index page
@route("/")
@view("index")
def index():
    pass

@route("/product_page")
@view("product_page")
def product_page():
    data = dict (item_list = items)
    return data







@route("/picture/<filename>")
def serve_picture(filename):   #need this for images to work on my website
    return static_file(filename, root ="./images")

run(host ='0.0.0.0', port = 8080, reloader = True, debug = True)