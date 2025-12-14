#ask user to input temperature outside
#conditions as follow
# 0 to negative temp ------- BELOW FREEZING
# 1 to 15 - Extreme Cold temperature
# 16 to 30 - Cold temperature
# 31 to 38 - Lukewarm Temperature
# 39 to 42 - Warm Temperature
# 43 to 50 - Hot Temperature
# 51 to 60 - Extremely Hot
# 61 and above - Burning Temperature


temp = eval(input("Enter Temperature ---> "))

if temp <= 1:
	print("Temperature is Exremely Cold")
elif temp >= 1 and temp <= 15:
	print("Temperature is Extremely Cold")
elif temp >= 16 and temp <= 30:
	print("Temperature is Cold")
elif temp >= 31 and temp <= 38:
	print("Temperature is Lukewarm")
elif temp >= 39 and temp <= 42:
	print("Temperature is Warm")
elif temp >= 43 and temp <= 50:
	print("Temperature is Hot")
elif temp >= 51 and temp <= 60:
	print("Temperature is Extremly Hot")
elif temp >= 61:
	print("Temperature is Burning Hot")
else:
	print("Invalid temperature")


