RUN = True
bag = []
print("Välkommen till påsen 🎒")
print("-" * 40)
while RUN:
    print("""
Visa innehållet i påsen [V]
Spara i påsen [S]
Leta i påsen [F]
Avsluta programmet [Q]""")
    choice = input("Välj: ")
    print("-" * 40)
    if choice.lower() == "v":
        print("I påsen hittar du:")
        for thing in bag:
            print(thing)
    elif choice.lower() == "s":
        bag.append(input("Skriv vad du vill spara i påsen: "))
    elif choice.lower() == "q":
        RUN = False
    elif choice.lower() == "f":
        query = input("Skriv vad du vill leta efter i påsen: ")
        if query.lower() in bag:
            print(f"Du rotar runt och hittar {query} i påsen.") 
        else:
            print(f"Du gräver och letar så djupt du kan efter {query}, men du har ingen tur.")
    else:
        print("Påsen accepterar dina intentioner, men förstår inte kommandot.")
