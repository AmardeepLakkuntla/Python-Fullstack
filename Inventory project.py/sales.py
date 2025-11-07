# from products import deduct_stock
sales=[
{
    'sale_id':'D01',
    'products':{
     'P01':100,
     'P02':50,
     'P03':10
    }
},
{
    'sale_id':'D02',
    'products':{
     'P01':10,
     'P04':5,
     'P05':6
    }
}
]

def add_sale(sale_id,product_id,qnty):
    if(product_id,qnty):
        sales.append(
            {
                'sale_id': sale_id,
                'product_id':product_id,
                'qnty':qnty
            })

        
def get_sales():
    return sales