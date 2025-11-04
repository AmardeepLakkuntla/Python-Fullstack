
text_1=int(input("enter the a : "))
text_2=int(input("enter the b : "))
sum = text_1+text_2
product = text_1 * (text_2)
result= (sum)*product
print(sum)
print(product)
print(result)

# Combo 3: If-elif-else
x = 1
if x > 6:
    print("Hello")
elif x > 1:
    print("Hello 2")
else:
    print("hello 3")

# Good indentation
x=5
if x > 10:
    print("Greater than 10")
    if x > 20:
        print("Greater than 20")
    print("Still in first if block")
print("Outside all if blocks")