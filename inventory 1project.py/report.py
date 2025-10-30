from products import products
 
 
def generate_report():
  for i in products:
         print("ID:", i['id'])
         print("Name:", i['name'])
         print("Price:", i['price'])
         print("Stock:", i['stock'])
print(f" Total No. of products: {len(products)}")
 
 
def check_alerts(threshold):
   
    for i in products:
        if i['stock'] <= threshold:
            print(f"{i['name']} has low stock {i['stock']}")