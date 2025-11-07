suppliers = [
    {
        'supplier_id': 'S01',
        'name':'shiva',
        'category':'grocery',
        'contact':8184941910
    },
    {
        'supplier_id': 'S02',
        'name':'veerabhadra',
        'category':'snacks',
        'contact':6281748974
    }
]
supplier_products={
    'S01':['grocery'],
    'S02':['snacks']
}

def add_supplier(supplier_id,name,category,contact):
    suppliers.append({
        'supplier_id':supplier_id,
        'name':name,
        'category':category,
        'contact':contact
    })
    print('successfully added')
    
    def get_supplier_products(supplier_id):
     if supplier_id in supplier_products:
        return supplier_products[supplier_id]
     else:
        return " No products found for this supplier."



    