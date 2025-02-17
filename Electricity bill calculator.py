#Python Functions to calculate the electricity bill.
customerId= int(input("Enter Customer's Id:"))
customerName = input("Enter Customer Name:")
unitConsumed= int(input("Enter Unit Consumed:"))
if unitConsumed < 200 :
        amount=1.20
        charges = unitConsumed * amount
        print("Fine to be paid=",charges)
elif unitConsumed >= 200:
        amount=1.50
        charges =unitConsumed * amount
        print("fine to be charged=", charges)
elif unitConsumed > 400:
        amount=1.80
        charges= unitConsumed * amount
        print("fine charged =", charges)
elif unitConsumed > 600:
        amount=2.0
        charges= unitConsumed * amount
        print("fine charged =", charges)
else :
        print("No fine charged")
if charges > 400 :
        newCharges = charges * 0.15
        print("Bill =:",newCharges)
else:
        print("the minimum bill should be 100")
print("CustomerID:",customerId)
print("Customer Name:", customerName)
print("Unit Consumed:", unitConsumed)
print("Charges per unit", amount)
print("Total Amount to pay =", newCharges)