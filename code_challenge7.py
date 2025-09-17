#Ask the user to enter a starting number
#USE A FOR LOOP THAT COUNTS FROM A USER-SPECIFIED NUMBER DOWN TO 1
#PRINT EACH NUMBER ON A NEW LINE
#THEN PRINT LIFTOFF!

print('⏳ COUNTDOWN TIMER SIMULATOR')
start = int(input('\nEnter a starting number---> '))
print('Starting countdown...')
for i in range(start, 0, -1):
    print(i)
    
print('Liftoff!')