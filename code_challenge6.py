# ODD NUMBER SUMMATION
# Enter 7 random numbers, then display the sum of all odd numbers

print("ODD NUMBER SUMMATION")

odd_sum = 0   # start with 0

for x in range(1, 8, 1):   
    nmbr = eval(input("Enter a number: "))
    if nmbr % 2 == 1:   
        odd_sum += nmbr

print("The sum of all odd numbers is", odd_sum)
