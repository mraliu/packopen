import random

money =  100
packcost = 5
pokemons = ["Bulbasaur", "Charmander", "Squirtle", "Pidgeot", "Jigglypuff"]

choice = ""

while choice != "quit":
    print("You have", 100, "credits")
    print("A pack cost", packcost)
    choice = input("Do you want to open a pack? ")

    if choice == "yes":
        if money > 4: 
            money = money - packcost
            randomnumber = random.randint(0, len(pokemons)-1)
            pokemon = pokemons[randomnumber]
            print("You have got! ", pokemon)
            print("You have ", money, "remaining.")
        else:
            print("You dont have enough money remaining.")