print("📚 Welcome to the Manga Recommender!")
print("Select your preferred genre:")
print("1. Action")
print("2. Seinen")
print("3. Sports")

genre_choice = input("Enter choice (1/2/3): ")

if genre_choice == "1":  
    decade = input("Which decade? (1990s/2000s/2010s): ").lower()
    length = input("How long should the manga be? (short/medium/long): ").lower()

    if decade == "1990s":
        if length == "short":
            print(" Recommendation: Battle Angel Alita")
        elif length == "medium":
            print(" Recommendation: Yu Yu Hakusho")
        else:
            print(" Recommendation: Hunter x Hunter")

    elif decade == "2000s":
        if length == "short":
            print(" Recommendation: Gantz")
        elif length == "medium":
            print(" Recommendation: Fullmetal Alchemist")
        else:
            print(" Recommendation: Naruto")

    elif decade == "2010s":
        if length == "short":
            print(" Recommendation: Fire Punch")
        elif length == "medium":
            print(" Recommendation: Dorohedoro")
        else:
            print(" Recommendation: One Punch Man")

elif genre_choice == "2":  
    decade = input("Which decade? (1990s/2000s/2010s): ").lower()
    length = input("How long should the manga be? (short/medium/long): ").lower()

    if decade == "1990s":
        if length == "short":
            print(" Recommendation: Parasyte")
        elif length == "medium":
            print(" Recommendation: Berserk")
        else:
            print(" Recommendation: Ghost in the Shell")

    elif decade == "2000s":
        if length == "short":
            print(" Recommendation: 20th Century Boys")
        elif length == "medium":
            print(" Recommendation: Homunculus")
        else:
            print(" Recommendation: Vagabond")

    elif decade == "2010s":
        if length == "short":
            print(" Recommendation: Inuyashiki")
        elif length == "medium":
            print(" Recommendation: Oyasumi Punpun")
        else:
            print(" Recommendation: Kingdom")

elif genre_choice == "3":  
    decade = input("Which decade? (1990s/2000s/2010s): ").lower()
    length = input("How long should the manga be? (short/medium/long): ").lower()

    if decade == "1990s":
        if length == "short":
            print(" Recommendation: Kyojin no Hoshi")
        elif length == "medium":
            print(" Recommendation: Ashita no Joe")
        else:
            print(" Recommendation: Slam Dunk")

    elif decade == "2000s":
        if length == "short":
            print(" Recommendation: Buzzer Beater")
        elif length == "medium":
            print(" Recommendation: Eyeshield 21")
        else:
            print(" Recommendation: Yowamushi Pedal")

    elif decade == "2010s":
        if length == "short":
            print(" Recommendation: The Climber")
        elif length == "medium":
            print(" Recommendation: Haikyuu!!")
        else:
            print(" Recommendation: Diamond no Ace")

else:
    print(" Invalid selection.")
