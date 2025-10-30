products = [
    {
        'id' : 1,
        'name' : 'Bat',
        'price' : 1000,
        'stock' : 500
 
    },
    {
        'id' : 2,
        'name' : 'Ball',
        'price' : 200,
        'stock' : 600
    },
    {
        'id' : 3,
        'name' : 'Helmet',
        'price' : 500,
        'stock' : 700
    },
    {
        'id' : 4,
        'name' : 'Gloves',
        'price' : 300,
        'stock' : 700
    }
]
 
def add_product(id,name,price,stock):
    products.append(
        {
            'id' : id,
            'name' : name,
            'price' : price,
            'stock' : stock
        }
    )
 
 
def update_stock(prod_id,qnty):
    for product in products:
        if product['id'] == prod_id:
            product['stock'] += qnty
            return
    print("Product not found !")
 
 
 
 
def deduct_stock(prod_id,qnty):
    for product in products:
        if product['id'] == prod_id:
             if product['stock'] >= qnty:
                product['stock'] -= qnty
                return True
             else:
                 return False
    return False
 
 
 
 
def get_all_products():
    return products
 
 
 
def view_prod_details(prod_id):
    for product in products:
        if product['id'] == prod_id:
            print(f"\nProduct ID: {product['id']}")
            print(f"Name: {product['name']}")
            print(f"Price: {product['price']}")
            print(f"Stock: {product['stock']}")
            return
    print("Product not found !")
 
 
def delete_product(prod_id):
    for product in products:
        if product['id'] == prod_id:
            products.remove(product)
            print(" Product deleted successfully")
            return
    print("Product not found")