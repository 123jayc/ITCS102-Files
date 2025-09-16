print("THE FACTORIAL program")

fctrl = 1
nmbr = eval(input("Enter any number --->"))
for x in range(nmbr, 0, -1):
	fctrl *= x

print("The factorial of", nmbr, "is", fctrl)