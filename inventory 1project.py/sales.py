from products import deduct_stock
 
sales = []
 
def add_sale(id,prod_id,qnty):
    if deduct_stock(prod_id,qnty):
        sales.append(
        {
            'id' : id,
            'product_id' : prod_id,
            'quantity' : qnty
        }
    )
        return True
    return False
 
 
def sales_details():
  return sales