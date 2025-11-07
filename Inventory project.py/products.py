products=[
    #  "P01":{
    {
        
        'product_id':'P01',
        'product_name':'sugar',
        'category':'grocery',
        'price':45,
        'stock':20
    },
    {
    #   "P02":{
        
        'product_id':'P02',
        'product_name':'oil',
        'category':'grocery',
        'price':150,
        'stock':15   
    },
    {
    #   "P03":{
        
        'product_id':'P03',
        'product_name':'haldiraims Mixture',
        'category':'snacks',
        'price':120,
        'stock':5
    },
    {
    #  "P04":{
        
        'product_id':'P04',
        'product_name':'thumsup',
        'category':'soft drinks',
        'price':100,
        'stock':9
    },
    {
    #  "P05":{
        'product_id':'P05',
        'product_name':'pedigree',
        'category':'pet supplies',
        'price':300,
        'stock':12
    }
    
]

def add_product(product_id,product_name,category,price,stock):
    products.append({
        'product_id':product_id,
        'product_name':product_name,
        'category':category,
        'price':price,
        'stock':stock
    })
    print('successfully added')
def update_product(product_id,new_stock):
    for product in products:
        if product["product_id"] == product_id:
            product["stock"]=new_stock
            print("product stock updated")
            break
        else:
            print("please enter coreect id and stock")
def remove_product(product_id):
    for product in products:
        if product['product_id']==product_id:
            products.remove(product)
            print('successfully deleted')
            break
        else:
            print("product not found")

def recorder_alert(product_id,qnty):
    if (product_id['stock']<=4):
        qnty='stock'
        {
            'product_id':product_id,
            "qnty":qnty
        }
        print(f'below thresold {qnty} total products:{qnty}')
    else:
        print(f'your stock is {qnty}')
def get_products():
    return products
