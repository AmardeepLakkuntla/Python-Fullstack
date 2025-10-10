#  COMBO 1
temp=int(input("enter the temperture: "))
if temp>9:
    print('it is cool')

    
#  COMBO 2
temp=int(input("enter the temperture: "))
if temp>9:
    print('it is cool')
else:
    print('it is hot')


#  COMBO 3
temp=int(input("enetr the temperature: "))
if temp>37:
    print("it is hot")
elif temp==37:
    print("it is moderate")
else:
    print("it is cool")


#   COMBO 4
temp=int(input("enetr the temperature: "))
if temp>37:
    print("it is hot")
elif temp==37:
    print("it is moderate")


#  NESTED CONDITION STATEMENTS
if 4+4==8:
    print("it is hot")
    if 5*5==25:
        print("amar")
else:
    print("shiva")

marks=int(input("enter the marks: "))
if marks>90:
    print("you passed with A+ grade")
elif marks>=80:
    print("you passed with A grade")
elif marks>=70:
    print("you passed with B grade")
elif marks>=50:
    print("you passed with C grade")
else:
    print("your are fail")