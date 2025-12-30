# Problem 4: Secure ATM Withdrawal System (Nested IF)

stored_pin = 4321
balance = 15000

entered_pin = int(input("Enter ATM PIN: "))

if entered_pin == stored_pin:
    amount = int(input("Enter withdrawal amount: "))
    
    if amount <= balance:
        if amount % 100 == 0:
            balance -= amount
            print("Withdrawal successful")
            print("Remaining balance:", balance)
        else:
            print("Amount must be multiple of 100")
    else:
        print("Insufficient balance")
else:
    print("Invalid PIN")