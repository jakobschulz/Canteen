from bottle import run, route, view, get, post, request, static_file  
from itertools import count

class Food_Item:
    _ids = count(0)
    
    def __init__(self, name, price, stock, image):  #makes these variables for each item of food
        self.id = next(self._ids)
        self.name = name
        self.price = price
        self.stock = stock
        self.image = image
        
#this is my class containg each of my food items.
items = [Food_Item("Sushi Roll", 9, 5,"sushi.jpg"), 
         Food_Item("Chips and Hot Dog", 7, 12,"Hot dogs.jpg"),
         Food_Item("Ham and Cheese Sandwich", 6, 4, "H&C sandwich.jpg")] 


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


@route('/purchase_page/<item_id>')
@view('purchase_page')
def purchase_page(item_id):
    item_id = int(item_id)
    found_item = None
    for item in items: 
        if item.id == item_id:
            found_item  = item
    data = dict (item = found_item)
    found_item.stock = found_item.stock - 1   #minus 1 from the amount of food items in stock
    return data 


@route("/restock_page")
@view("restock_page")
def restock_page():
    data = dict (item_list = items)
    return data

@route('/restock_success/<item_id>', method='POST')
@view('restock_success')
def restock_page(item_id):
    item_id = int(item_id)
    found_item = None
    for item in items: 
        if item.id == item_id:
            found_item  = item
    data = dict (item = found_item)
    restock_add = request.forms.get('restock_add')
    restock_add =int(restock_add)
    found_item.stock = found_item.stock + restock_add
    pass




@route("/images/<filename>")
def serve_picture(filename):   #need this for images to work on my website
    return static_file(filename, root ="./images")

run(host ='0.0.0.0', port = 8080, reloader = True, debug = True)
