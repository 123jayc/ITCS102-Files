#Dictionary

fruits = ['Apple', 'Banana', 'Cherry', 'Mango', 'Grapes', 'Orange', 'Pineapple']
#           0         1         2        3         4         5          6  
print(fruits[-1])

# {Keys : Values, Keys : Values}    
fruit_dictionary = {'sweet':'Apple', 'tropical':'Banana', 'small':'Cherry', 'juicy':'Mango', 'seeded':'Grapes', 'citrus':'Orange', 'exotic':'Pineapple'}
print(fruit_dictionary['seeded'])

# Adding item
fruit_dictionary['classic'] = 'Strawberry'
print(fruit_dictionary)

# Removing item
fruit_dictionary.pop('citrus')
print(fruit_dictionary)