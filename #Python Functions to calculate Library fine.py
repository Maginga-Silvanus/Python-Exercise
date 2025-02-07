#Python Functions to calculate fine overdue in library
bookId= int(input("Enter Book Id:"))
dueDate = int(input("Enter due date:"))
returnDate= int(input("Enter Return date:"))
daysOverdue = returnDate- dueDate
if daysOverdue <= 7 :
        charges = daysOverdue * 20
        print("Fine to be paid=",charges)
elif daysOverdue >=8:
        charges =daysOverdue * 50
        print("fine to be charged=", charges)
elif daysOverdue >14:
        charges= daysOverdue * 100
        print("fine charged =", charges)
else :
        print("No fine charged")
print("bookId",bookId)
print("dueDate", dueDate)
print("returndate", returnDate)
print("daysOverdue", daysOverdue)
print("fine rate=", charges)

