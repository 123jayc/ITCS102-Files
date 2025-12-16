length = 15.5
width = 8.2

# Calculate
area = length * width

#  String Formatting using f strings 

print(f" Dimensions:")
print(f" Length: {length} meters")
print(f" Width:  {width} meters")

print(f"\n Calculation:")
print(f" Area = Length * Width")
print(f" Area = {length} * {width}")
print(f" The total area of the rectangle is {area:.2f} square meters.")

# upper and capitalized letter
shape = "rectangle"
print(f"Name (UPPERCASE): {shape.upper()}")
print(f"Name (Capitalized letter): {shape.capitalize()}")