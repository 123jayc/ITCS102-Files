#Create a program that prints the of a number entered by the user, using a simple for loop.
#Ask the user to input a number.Use a for loop to print the multiplication table from for that number.
# Format each line clearly (e.g., 5 x 1 = 5).

#This reinforces:
#Looping over a fixed range (range(1, 11))
#Using the loop variable in calculations
#String formatting


print('MULTIPLICATION TABLE MAKER')
mul = int(input('Enter a number:'))
print('Multiplacation table for', mul, ':')
for i in range(1, 11):
    print(mul, 'x', i, '=', mul * i)
