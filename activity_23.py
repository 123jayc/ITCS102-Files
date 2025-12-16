#list of favorite music genres
genres = ["Rock", "Classical", "Jazz", "OPM", "R&B"]
#           0          1          2      3      4
print(f"Original Genre List:\n{genres}\n")

#Add a new genre to the end of the list
genres.append("Folk")
print(f"After using .append('Folk'):\n{genres}\n")

#insert a genre at a specific position 
genres.insert(1, "Pop")
print(f"After using .insert(1, 'Pop'):\n{genres}\n")

# Remove 
genres.remove("R&B")
print(f"After using .remove('R&B'):\n{genres}\n")

#Remove the last genre from the list 
removed_genre = genres.pop() # 'Folk' is removed and stored
print(f"After using .pop():\n{genres}")
print(f"The genre removed by .pop() was: {removed_genre}\n")

#length of the list
current_count = len(genres)
print(f"Total number of favorite genres now: {current_count}\n")

#sort the list alphabetically
genres.sort()
print(f"Genre List:\n{genres}\n")

print("My Top Genres (2025 List):")
for genre in genres:
    print(f"I love listening to {genre}!")