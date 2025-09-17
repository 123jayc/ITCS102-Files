# Create a fun program that acts like a parrot — it repeats anything 
# the user says, using a for loop to "squawk" it back multiple times!
# Ask the user to enter a phrase (e.g., "I love Python!").
# Ask how many times they want the parrot to repeat it.
# Use a for loop to print the phrase that many times.
# Make each line sound like a parrot: " Squawk! {phrase}"   
#Listen to your parrot:
#🦜 Squawk! I am hungry!

print("🦜 PARROT SIMULATOR – THE ECHO CHAMBER!")
phrase = input('Enter a phraase for the parrot to repeat: ')
times = int(input('How many times do you want the parrot to repeat the phrase?'))
print('Listen to your parrot:')
for i in range(times, 0, -1):
  print('🦜 Squawk!', phrase)