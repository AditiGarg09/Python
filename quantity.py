quantity=int(input("Enter Quantity: "))
price=quantity*100
if(price>1000):
    discount=int(price*0.1)
    price-=discount
    print("Price is",int(price))
else:
    print("Price is",price)
