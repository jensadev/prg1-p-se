run = True
bag = []
print("Välkommen till påsen 🎒")
while run:
    print("Visa innehållet i påsen [V]")
    print("Spara i påsen [S]")
    print("Avsluta programmet [Q]")
    choice = input("Välj: ")
    if choice.lower() == "v":
        for thing in bag:
            print(thing)
    elif choice.lower() == "s":
        bag.append(input("Skriv vad du vill spara: "))
    elif choice.lower() == "q":
        run = False
    else:
        print("Felaktigt kommando, försök igen.")
