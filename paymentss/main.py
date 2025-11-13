from paytm import *
from phonepe import *
amount=int(input("enter the amount: "))
mode=input("paytm or phonepe: ")
if mode == "paytm":
    paytm_payment(amount)
elif mode == "phonepe":
    phonepay_pay(amount)