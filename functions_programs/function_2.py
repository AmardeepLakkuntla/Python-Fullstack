def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
check_number=int(input("enter anumber:"))

print(check_even_odd(check_number))
