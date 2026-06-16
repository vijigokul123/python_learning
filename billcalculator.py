print("="*50)
print("     SMART BILL CALCULATOR")
print("="*50)
Customer_name=input("Enter your name:")
Item_name=input("Enter item name:")
Price=float(input("Enter price:"))
Quantity=int(input("Enter no of items purchased:"))
Total=Price*Quantity

print("\n Memebership Options:")
print("1.Premium member")
print("2.Regular member")

choice=int(input("choose 1 or 2"))

if(choice==1):
    discount=Total*0.10
    Final_amt=Total-discount
    member_type="Premium"

else:
    discount=0
    Final_amt=Total
    member_type="Regular"

print("\n")
print("="*50)
print("Bill Summary")
print("="*50)

print("Customer name:",Customer_name)
print("Item name:",Item_name)
print("Price:",Price)
print("Quantity:",Quantity)
print("Total amount:",Total)
print("Member type:",member_type)
print("Discount:",discount)
print("Final Amount:",Final_amt)

print("="*50)
print("Thank you for shopping")
