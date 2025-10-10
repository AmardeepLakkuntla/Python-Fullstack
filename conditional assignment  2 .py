username=("amardeep")
password=("Amar")
text=input("enter the username")
text_1=input("enter the password")
if username==text:
    #print(" valid username ")
    if password==text_1:
        print("successfully login done")
    #elif username!=text:
        #print("invalid username")
    elif password!=text_1:
        print("invalid password")
else:
    print("your username and password is not valid")
    