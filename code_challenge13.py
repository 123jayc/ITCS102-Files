user_name = input("Input your name here ---> ")
print("Hi", user_name, "Welcome to the ODD NUMBER SUMMATION PROGRAM")
print("Enter any random number. Press 0 if you want the program to stop\n")

is_running = True

odd_sum = 0

odd_numbers_list = "" 

while is_running:

    try:
        input_value = int(input("Input any number: "))
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        continue

    if input_value % 2 != 0: 
        print("Odd Number Detected, proceed to next number ")
        odd_sum += input_value
        odd_numbers_list += str(input_value) + " "
        continue

    elif input_value == 0:
        print("Program END. ")
        is_running = False 
        break

    else:
        print("Even Number Detected, proceed to next number ")

print(f"\n--- RESULTS ---")
print(f"Hi {user_name}, the total sum of all odd numbers is {odd_sum}")
print(f"ODD numbers detected: {odd_numbers_list}")