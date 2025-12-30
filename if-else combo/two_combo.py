# Problem 2: Online Shopping Discount System (IF-ELSE)

customer = input("Enter customer name: ")
bill_amount = float(input("Enter total bill amount: "))

if bill_amount >= 5000:
    discount = bill_amount * 0.10
    final_amount = bill_amount - discount
    print(customer, "you received a discount of", discount)
    print("Final amount to pay:", final_amount)
else:
    print(customer, "no discount applied")
    print("Final amount to pay:", bill_amount)