#ask user for an item price
#quantity
#if cost is above 100, apply discount of 10%

price = eval(input("Input Item Price ----> $"))
quantity = eval(input("Item Quantity --> "))

cost = price * quantity

print("Total cost $", cost)

if cost >= 100:
	discount = cost * 0.10
	final_cost = cost - discount
	print("Discounted price is $", final_cost)
else:
	print("No discount applied")

