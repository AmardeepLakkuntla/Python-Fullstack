from products import add_product,get_products,remove_product,update_product,recorder_alert
from suppliers import add_supplier
from sales import add_sale,get_sales
from reports import generate_report,check_alerts
def show_menu():
    print('''
            1. Add New Product
            2. Update Product Stock
            3. Record a Sale
            4. Add Supplier
            5. Generate Inventory Report
            6. Check Reorder Alerts
            7. View Product Details
            8. Delete a Product
            9.view all sales
            10. Exit
''')


def main():
    while True:
     show_menu()
     choice=input('enter your choie: ')
     if choice == '1':
        product_id= input('enter id: ')
        product_name=input('enter product name: ')
        category= input('enter category : ')
        price=int(input('enter price: '))
        stock=int(input('enter stock: '))
        add_product(product_id,product_name,category,price,stock)
     elif choice=='2':
            product_id = input("Enter Product ID: ")
            new_stock = int(input("Enter new stock: "))
            update_product(product_id, new_stock)
     elif choice == '3':
            sale_id = input("Enter Sale ID: ")
            prod_id = input("Enter Product ID: ")
            qnty = int(input("Enter Quantity Sold: "))
            if add_sale(sale_id,prod_id,qnty):
                print("Sale Recorded!")
            else:
                print("Not enough stock!")
     elif choice=='4':
         supplier_id=input('enter id: ')
         name=input('enter name: ')
         category=input('enter category: ')
         contact=int(input('enter contact: '))
         add_supplier(supplier_id,name,category,contact)
     elif choice == '5':
            generate_report()
     elif choice == '6':
            threshold = int(input("Enter Re-order Threshold: "))
            check_alerts(threshold)
     elif choice=='7':
        products= get_products()
        print(products)
     elif choice=='8': 
         iden=input('enter id:')
         remove_product(iden)
     elif choice=='9':
         sales=get_sales()
         print(sales)
     elif choice=='10':
        print("thank you for visiting the store")
        break
    else:
        print("invalid choice")
       
         
  
     
  
         
         
        


if __name__=='__main__':
    main()