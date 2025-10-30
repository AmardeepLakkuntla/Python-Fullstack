suppliers = [
    {
        'id' : 1,
        'name' : 'Raju',
        'contact' : 500600
    },
    {
        'id' : 2,
        'name' : 'Suresh',
        'contact' : 500063
    },
    {
        'id' : 3,
        'name' : 'Mohan',
        'contact' : 515801
    }
]
supplier_products = {
 
     1 : ['Bat', 'Ball'],
     2 : ['Gloves'],
     3 : ['Helmet']
}
 
 
 
def add_supplier(sup_id,name,contact):
    suppliers.append(
        {
            'id' : sup_id,
            'name' : name,
            'contact' : contact
        }
    )
    print(" Supplier added successfully !")
 
 
 
 
def get_sup_products(sup_id):
    if sup_id in supplier_products:
        return supplier_products[sup_id]
    else:
        return " No products found for this supplier."