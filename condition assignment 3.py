secret=5
text=int(input("guess the number: "))
if text>secret:
    print("you are too high")
elif text<secret:
    print("your are too low")
else:
    print("your are correct")
    