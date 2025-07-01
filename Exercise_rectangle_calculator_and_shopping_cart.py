#RECTANGLE AREA CALCULATOR

#for super script 2 or power 2 on the numlock + alt + 0178
length=float(input("enter your length:"))
width=float(input("enter your width:"))
area =length*width
print(f"the area is {area}cm²")

#SHOPPING CART PROGRAM
item=input("what would you like to buy?:")
price =float(input("what is the price?:"))
quantity=int(input("how many would you like?:"))
total=price*quantity

print(f"you have brought {quantity} {item}")
print(f"your total is $ {total}")
