from products import products

def generate_report():
  for i in products:
         print("ID:", i['product_id'])
         print("Name:", i['product_name'])
         print("Price:", i['price'])
         print("Stock:", i['stock'])
print(f" Total No. of products: {len(products)}")


def check_alerts(threshold):
   
    for i in products:
        if i['stock'] <= threshold:
            print(f"{i['product_name']} has low stock {i['stock']}")

