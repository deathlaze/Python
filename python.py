price=1000000
good_credit=True
not_good_credit=False

if good_credit:
    down_payment=price/10
    
elif not_good_credit:
       down_payment=price/5
print(f"down payment:{down_payment}")

