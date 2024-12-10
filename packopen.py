import random

pokemons = ["Bulbasaur", "Charmander", "Squirtle", "Pidgeot", "Jigglypuff"]

choice = ""

while choice != "quit":
    choice = input("Do you want to open a pack? ")

    if choice == "yes":
        randomnumber = random.randint(0, len(pokemons)-1)
        pokemon = pokemons[randomnumber]

        print("You have got! ", pokemon)