from bottle import run, route, view, get, post, request, static_file   #imports tools from bottle
from itertools import count

class Food_Item:
    _ids = count(0)
    
    def __init__(self, name, price, stock, image, amount_sold):  #makes these variables for each item of food
        self.id = next(self._ids)
        self.name = name
        self.price = price
        self.stock = stock
        self.image = image
        self.amount_sold = amount_sold
        
#this is my class containg each of my food items.
items = [Food_Item("Sushi Roll", 9, 5,"sushi.jpg", 0), 
         Food_Item("Chips and Hot Dog", 7, 12,"Hot dogs.jpg", 0),
         Food_Item("Ham and Cheese Sandwich", 6, 4, "H&C sandwich.jpg", 0)] 


#index page
#needed to attach decorators to and to create the page.
@route("/")
@view("index")
def index():
    pass

#product page
@route("/product_page")
@view("product_page")
def product_page():
    data = dict (item_list = items) #makes a dictionary of my food items
    return data #pretty self explanitory, returns data

#purchase page
@route('/purchase_page/<item_id>', method='POST') #uses the method post to get the input from my online form
@view('purchase_page')
def purchase_page(item_id): #passes purchase_page item_id
    purchase_amount = request.forms.get("purchase_amount")    #gets information from my form
    purchase_amount = int(purchase_amount)                    #makes sure purchase_amount is an integer

    item_id = int(item_id) #makes sure item_id is a number
    found_item = None
    for item in items:     #for each item in items it does the below process
        if item.id == item_id: #looks through items to find the item that was clicked on
            found_item  = item #makes that item found item
    data = dict (item = found_item)   #makes a dictionary of found item
    found_item.stock = found_item.stock-purchase_amount #minuses the amount of stock the user buys from item stock
    found_item.amount_sold = found_item.amount_sold + purchase_amount #adds the amount of stock the user buys to the amount of that stock sold          
    return data 

#restock page
@route("/restock_page")
@view("restock_page")
def restock_page():
    data = dict (item_list = items) #makes a dictionary of my food items
    return data #returns that dictionary

@route('/restock_success/<item_id>', method='POST') #uses the method post to get the input from my online form
@view('restock_success')
def restock_page(item_id): #passes restock_page item_id
    restock_add = request.forms.get('restock_add') #gets info from html form
    item_id = int(item_id) #makes sure item_id is a number 
    found_item = None 
    for item in items:     #does the below for each item in items
        if item.id == item_id: #checks to see for each item in items if the item it is scanning is the item was the item that was clicked on
            found_item  = item 
    data = dict (item = found_item) #makes a dictionary of found item
    
    restock_add =int(restock_add)
    found_item.stock = found_item.stock + restock_add #adds stock to stock amount
    pass




@route("/images/<filename>")
def serve_picture(filename):   #need this for images to work on my website
    return static_file(filename, root ="./images") 

run(host ='0.0.0.0', port = 8080, reloader = True, debug = True) #runs server on localhost:8080
