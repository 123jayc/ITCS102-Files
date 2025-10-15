Clone = True 
sum = 0
while Clone == True:
    confirm = input("Do you wish to continue cloning? ( y / n)").lower()
    sum += 1
    if confirm == 'y':
        print('Cloning Continues.....')
        continue
    else:
        print('Cloning Stops....')
        break

print(f'Number of clones is {sum}')
