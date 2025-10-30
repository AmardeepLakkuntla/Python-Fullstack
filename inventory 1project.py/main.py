from products import get_all_products,add_product,update_stock,view_prod_details,delete_product                                                                                                            
from sales import sales_details,add_sale
from suppliers import add_supplier,get_sup_products
from report import generate_report,check_alerts
 
def show_menu():
    print('''
            1. View All Products
            2. Add New Product
            3. Update Product Stock
            4. Record a Sale
            5. View Sales
            6. Add Supplier
            7. View Supplier's Products
            8. Generate Inventory Report
            9. Check Re-order Alerts
           10. View Product Details
           11. Delete a Product
           12. Exit
    ''')
 
 
def main():
 
    while True:
        show_menu()
        choice = input('Enter your choice:')
 
        if choice == '1':
            products = get_all_products()
            print(products)
 
        elif choice == '2':
            id = int(input("Enter Product ID: "))
            name = input("Enter Product Name: ")
            price = int(input("Enter Price: "))
            stock = int(input("Enter Stock: "))
            add_product(id, name, price, stock)
            print(" Product added!")
           
        elif choice == '3':
            prod_id = int(input("Enter Product ID: "))
            qnty = int(input("Enter Stock to Add: "))
            update_stock(prod_id, qnty)
            print("Stock Updated!")
 
        elif choice == '4':
            sale_id = int(input("Enter Sale ID: "))
            prod_id = int(input("Enter Product ID: "))
            qnty = int(input("Enter Quantity Sold: "))
            if add_sale(sale_id,prod_id,qnty):
                print("Sale Recorded!")
            else:
                print("Not enough stock!")
 
        elif choice == '5':
            print(sales_details())
 
        elif choice == '6':
            sup_id = int(input("Enter Supplier ID: "))
            name = input("Enter Supplier Name: ")
            contact = input("Enter Supplier Contact: ")
            add_supplier(sup_id, name, contact)
 
        elif choice == '7':
            sup_id = int(input("Enter Supplier ID: "))
            print(get_sup_products(sup_id))
 
        elif choice == '8':
            generate_report()
 
        elif choice == '9':
            threshold = int(input("Enter Re-order Threshold: "))
            check_alerts(threshold)
 
        elif choice == '10':
            prod_id = int(input("Enter Product ID: "))
            view_prod_details(prod_id)
 
        elif choice == '11':
            prod_id = int(input("Enter Product ID to delete: "))
            delete_product(prod_id)
 
        elif choice == '12':
            print("Exiting !!!")
            break
 
        else:
            print("Invalid Option!")
 
 
 
if __name__ == '__main__':
    main()