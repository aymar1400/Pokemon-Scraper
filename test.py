import string
from bs4 import BeautifulSoup
import requests

# (0) Normal, (1) Fire, (2) Water,  (3) Grass, (4) Electric, (5) Ice, (6) Fighting, 
# (7) Poison, (8) Ground, (9) Flying, (10) Psychic, (11) Bug, (12) Rock, (13) Ghost, 
# (14) Dragon, (15) Dark, (16) Steel, (17) Fairy

normal = [1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1]
fire = [1, 0.5, 2, 0.5, 1, 0.5, 1, 1, 2, 1, 1, 0.5, 2, 1, 1, 1, 0.5, 0.5]
water = [1, 0.5, 0.5, 2, 2, 0.5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.5, 1]
grass = [1, 2, 0.5, 0.5, 0.5, 2, 1, 2, 0.5, 2, 1, 2, 1, 1, 1, 1, 1, 1]
electric = [1, 1, 1, 1, 0.5, 1, 1, 1, 2, 0.5, 1, 1, 1, 1, 1, 1, 0.5, 1]
ice = [1, 2, 1, 1, 1, 0.5, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1]
fighting = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 0.5, 0.5, 1, 1, 0.5, 1, 2]
poison = [1, 1, 1, 0.5, 1, 1, 0.5, 0.5, 2, 1, 2, 0.5, 1, 1, 1, 1, 1, 0.5]

ground = [1, 1, 2, 2, 0, 2, 1, 0.5, 1, 1, 1, 1, 0.5, 1, 1, 1, 1, 1]
flying = [1, 1, 1, 0.5, 2, 2, 0.5, 1, 0, 1, 1, 0.5, 2, 1, 1, 1, 1, 1]
psychic = [1, 1, 1, 1, 1, 1, 0.5, 1, 1, 1, 0.5, 2, 1, 2, 1, 2, 1, 1]
bug = [1, 2, 1, 0.5, 1, 1, 0.5, 1, 0.5, 2, 1, 1, 2, 1, 1, 1, 1, 1]
rock = [0.5, 0.5, 2, 2, 1, 1, 2, 0.5, 2, 0.5, 1, 1, 1, 1, 1, 1, 2, 1]
ghost = [0, 1, 1, 1, 1, 1, 0, 0.5, 1, 1, 1, 0.5, 1, 2, 1, 2, 1, 1]
dragon = [1, 0.5, 0.5, 0.5, 0.5, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2]
dark = [1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 0, 2, 1, 0.5, 1, 0.5, 1, 2]
steel = [0.5, 2, 1, 0.5, 1, 0.5, 2, 0, 2, 0.5, 0.5, 0.5, 0.5, 1, 0.5, 1, 0.5, 0.5]
fairy = [1, 1, 1, 1, 1, 1, 0.5, 2, 1, 1, 1, 0.5, 1, 1, 0, 0.5, 2, 1]

doubleWeak = []
weaknesses = []
neutral = []
resistances = []
doubleResist = []
immunities = []

inputPokemon = input("Enter a pokemon: ")
pokemonLength = len(inputPokemon)

urlString = "https://pokemondb.net/pokedex/" + inputPokemon


html_text = requests.get(urlString).text
soup = BeautifulSoup(html_text, 'lxml')
types = soup.find('div', class_ = "grid-col span-md-6 span-lg-8").text

index = pokemonLength + 7
index2 = types.find('type') - 1
pokemonType = types[index:index2]

slashIndex = pokemonType.find('/')

nOfTypes = 1

if slashIndex != -1:
    print(pokemonType)
    type1 = pokemonType[0:slashIndex]
    type2 = pokemonType[slashIndex+1:len(pokemonType)]
    if (type1 == "Normal"):
        type1 = normal
    elif (type1 == "Fire"):
        type1 = fire
    elif (type1 == "Water"):
        type1 = water
    elif (type1 == "Grass"):
        type1 = grass
    elif (type1 == "Electric"):
        type1 = electric
    elif (type1 == "Ice"):
        type1 = ice
    elif (type1 == "Fighting"):
        type1 = fighting
    elif (type1 == "Poison"):
        type1 = poison
    elif (type1 == "Ground"):
        type1 = ground
    elif (type1 == "Flying"):
        type1 = flying
    elif (type1 == "Psychic"):
        type1 = psychic
    elif (type1 == "Bug"):
        type1 = bug
    elif (type1 == "Rock"):
        type1 = rock
    elif (type1 == "Ghost"):
        type1 = ghost
    elif (type1 == "Dragon"):
        type1 = dragon
    elif (type1 == "Dark"):
        type1 = dark
    elif (type1 == "Steel"):
        type1 = steel
    elif (type1 == "Fairy"):
        type1 = fairy
    if (type2 == "Normal"):
        type2 = normal
    elif (type2 == "Fire"):
        type2 = fire
    elif (type2 == "Water"):
        type2 = water
    elif (type2 == "Grass"):
        type2 = grass
    elif (type2 == "Electric"):
        type2 = electric
    elif (type2 == "Ice"):
        type2 = ice
    elif (type2 == "Fighting"):
        type2 = fighting
    elif (type2 == "Poison"):
        type2 = poison
    elif (type2 == "Ground"):
        type2 = ground
    elif (type2 == "Flying"):
        type2 = flying
    elif (type2 == "Psychic"):
        type2 = psychic
    elif (type2 == "Bug"):
        type2 = bug
    elif (type2 == "Rock"):
        type2 = rock
    elif (type2 == "Ghost"):
        type2 = ghost
    elif (type2 == "Dragon"):
        type2 = dragon
    elif (type2 == "Dark"):
        type2 = dark
    elif (type2 == "Steel"):
        type2 = steel
    elif (type2 == "Fairy"):
        type2 = fairy
    
    pokemonType = []
    for i in range(0, len(normal)):
        pokemonType.append(type1[i] * type2[i])
else: # Single Type
    print(pokemonType)
    if (pokemonType == "Normal"):
        pokemonType = normal
    elif (pokemonType == "Fire"):
        pokemonType = fire
    elif (pokemonType == "Water"):
        pokemonType = water
    elif (pokemonType == "Grass"):
        pokemonType = grass
    elif (pokemonType == "Electric"):
        pokemonType = electric
    elif (pokemonType == "Ice"):
        pokemonType = ice
    elif (pokemonType == "Fighting"):
        pokemonType = fighting
    elif (pokemonType == "Poison"):
        pokemonType = poison
    elif (pokemonType == "Ground"):
        pokemonType = ground
    elif (pokemonType == "Flying"):
        pokemonType = flying
    elif (pokemonType == "Psychic"):
        pokemonType = psychic
    elif (pokemonType == "Bug"):
        pokemonType = bug
    elif (pokemonType == "Rock"):
        pokemonType = rock
    elif (pokemonType == "Ghost"):
        pokemonType = ghost
    elif (pokemonType == "Dragon"):
        pokemonType = dragon
    elif (pokemonType == "Dark"):
        pokemonType = dark
    elif (pokemonType == "Steel"):
        pokemonType = steel
    elif (pokemonType == "Fairy"):
        pokemonType = fairy
    



def my_function(listVar):
    for i in range(18):
        if (i == 0):
            if (listVar[i] == 0):
                immunities.append("Normal")
            elif (listVar[i] == 0.25):
                doubleResist.append("Normal")
            elif (listVar[i] == 0.5):
                resistances.append("Normal")
            elif (listVar[i] == 1):
                neutral.append("Normal")
            elif (listVar[i] == 2):
                weaknesses.append("Normal")
            elif (listVar[i] == 4):
                doubleWeak.append("Normal")
        elif (i == 1):
            if (listVar[i] == 0):
                immunities.append("Fire")
            elif (listVar[i] == 0.25):
                doubleResist.append("Fire")
            elif (listVar[i] == 0.5):
                resistances.append("Fire")
            elif (listVar[i] == 1):
                neutral.append("Fire")
            elif (listVar[i] == 2):
                weaknesses.append("Fire")
            elif (listVar[i] == 4):
                doubleWeak.append("Fire")
        elif (i == 2):
            if (listVar[i] == 0):
                immunities.append("Water")
            elif (listVar[i] == 0.25):
                doubleResist.append("Water")
            elif (listVar[i] == 0.5):
                resistances.append("Water")
            elif (listVar[i] == 1):
                neutral.append("Water")
            elif (listVar[i] == 2):
                weaknesses.append("Water")
            elif (listVar[i] == 4):
                doubleWeak.append("Water")
        elif (i == 3):
            if (listVar[i] == 0):
                immunities.append("Grass")
            elif (listVar[i] == 0.25):
                doubleResist.append("Grass")
            elif (listVar[i] == 0.5):
                resistances.append("Grass")
            elif (listVar[i] == 1):
                neutral.append("Grass")
            elif (listVar[i] == 2):
                weaknesses.append("Grass")
            elif (listVar[i] == 4):
                doubleWeak.append("Grass")
        elif (i == 4):
            if (listVar[i] == 0):
                immunities.append("Electric")
            elif (listVar[i] == 0.25):
                doubleResist.append("Electric")
            elif (listVar[i] == 0.5):
                resistances.append("Electric")
            elif (listVar[i] == 1):
                neutral.append("Electric")
            elif (listVar[i] == 2):
                weaknesses.append("Electric")
            elif (listVar[i] == 4):
                doubleWeak.append("Electric")
        elif (i == 5):
            if (listVar[i] == 0):
                immunities.append("Ice")
            elif (listVar[i] == 0.25):
                doubleResist.append("Ice")
            elif (listVar[i] == 0.5):
                resistances.append("Ice")
            elif (listVar[i] == 1):
                neutral.append("Ice")
            elif (listVar[i] == 2):
                weaknesses.append("Ice")
            elif (listVar[i] == 4):
                doubleWeak.append("Ice")
        elif (i == 6):
            if (listVar[i] == 0):
                immunities.append("Fighting")
            elif (listVar[i] == 0.25):
                doubleResist.append("Fighting")
            elif (listVar[i] == 0.5):
                resistances.append("Fighting")
            elif (listVar[i] == 1):
                neutral.append("Fighting")
            elif (listVar[i] == 2):
                weaknesses.append("Fighting")
            elif (listVar[i] == 4):
                doubleWeak.append("Fighting")
        elif (i == 7):
            if (listVar[i] == 0):
                immunities.append("Poison")
            elif (listVar[i] == 0.25):
                doubleResist.append("Poison")
            elif (listVar[i] == 0.5):
                resistances.append("Poison")
            elif (listVar[i] == 1):
                neutral.append("Poison")
            elif (listVar[i] == 2):
                weaknesses.append("Poison")
            elif (listVar[i] == 4):
                doubleWeak.append("Poison")
        elif (i == 8):
            if (listVar[i] == 0):
                immunities.append("Ground")
            elif (listVar[i] == 0.25):
                doubleResist.append("Ground")
            elif (listVar[i] == 0.5):
                resistances.append("Ground")
            elif (listVar[i] == 1):
                neutral.append("Ground")
            elif (listVar[i] == 2):
                weaknesses.append("Ground")
            elif (listVar[i] == 4):
                doubleWeak.append("Ground")
        elif (i == 9):
            if (listVar[i] == 0):
                immunities.append("Flying")
            elif (listVar[i] == 0.25):
                doubleResist.append("Flying")
            elif (listVar[i] == 0.5):
                resistances.append("Flying")
            elif (listVar[i] == 1):
                neutral.append("Flying")
            elif (listVar[i] == 2):
                weaknesses.append("Flying")
            elif (listVar[i] == 4):
                doubleWeak.append("Flying")
        elif (i == 10):
            if (listVar[i] == 0):
                immunities.append("Psychic")
            elif (listVar[i] == 0.25):
                doubleResist.append("Psychic")
            elif (listVar[i] == 0.5):
                resistances.append("Psychic")
            elif (listVar[i] == 1):
                neutral.append("Psychic")
            elif (listVar[i] == 2):
                weaknesses.append("Psychic")
            elif (listVar[i] == 4):
                doubleWeak.append("Psychic")
        elif (i == 11):
            if (listVar[i] == 0):
                immunities.append("Bug")
            elif (listVar[i] == 0.25):
                doubleResist.append("Bug")
            elif (listVar[i] == 0.5):
                resistances.append("Bug")
            elif (listVar[i] == 1):
                neutral.append("Bug")
            elif (listVar[i] == 2):
                weaknesses.append("Bug")
            elif (listVar[i] == 4):
                doubleWeak.append("Bug")
        elif (i == 12):
            if (listVar[i] == 0):
                immunities.append("Rock")
            elif (listVar[i] == 0.25):
                doubleResist.append("Rock")
            elif (listVar[i] == 0.5):
                resistances.append("Rock")
            elif (listVar[i] == 1):
                neutral.append("Rock")
            elif (listVar[i] == 2):
                weaknesses.append("Rock")
            elif (listVar[i] == 4):
                doubleWeak.append("Rock")
        elif (i == 13):
            if (listVar[i] == 0):
                immunities.append("Ghost")
            elif (listVar[i] == 0.25):
                doubleResist.append("Ghost")
            elif (listVar[i] == 0.5):
                resistances.append("Ghost")
            elif (listVar[i] == 1):
                neutral.append("Ghost")
            elif (listVar[i] == 2):
                weaknesses.append("Ghost")
            elif (listVar[i] == 4):
                doubleWeak.append("Ghost")
        elif (i == 14):
            if (listVar[i] == 0):
                immunities.append("Dragon")
            elif (listVar[i] == 0.25):
                doubleResist.append("Dragon")
            elif (listVar[i] == 0.5):
                resistances.append("Dragon")
            elif (listVar[i] == 1):
                neutral.append("Dragon")
            elif (listVar[i] == 2):
                weaknesses.append("Dragon")
            elif (listVar[i] == 4):
                doubleWeak.append("Dragon")
        elif (i == 15):
            if (listVar[i] == 0):
                immunities.append("Dark")
            elif (listVar[i] == 0.25):
                doubleResist.append("Dark")
            elif (listVar[i] == 0.5):
                resistances.append("Dark")
            elif (listVar[i] == 1):
                neutral.append("Dark")
            elif (listVar[i] == 2):
                weaknesses.append("Dark")
            elif (listVar[i] == 4):
                doubleWeak.append("Dark")
        elif (i == 16):
            if (listVar[i] == 0):
                immunities.append("Steel")
            elif (listVar[i] == 0.25):
                doubleResist.append("Steel")
            elif (listVar[i] == 0.5):
                resistances.append("Steel")
            elif (listVar[i] == 1):
                neutral.append("Steel")
            elif (listVar[i] == 2):
                weaknesses.append("Steel")
            elif (listVar[i] == 4):
                doubleWeak.append("Steel")
        elif (i == 17):
            if (listVar[i] == 0):
                immunities.append("Fairy")
            elif (listVar[i] == 0.25):
                doubleResist.append("Fairy")
            elif (listVar[i] == 0.5):
                resistances.append("Fairy")
            elif (listVar[i] == 1):
                neutral.append("Fairy")
            elif (listVar[i] == 2):
                weaknesses.append("Fairy")
            elif (listVar[i] == 4):
                doubleWeak.append("Fairy")


print("")
my_function(pokemonType)
print("Double Weak: " + str(doubleWeak))
print("Weak: " + str(weaknesses))
print("Neutral: " + str(neutral))
print("Resist: " + str(resistances))
print("Double resist: " + str(doubleResist))
print("Immunities: " + str(immunities))

test = input()

#print(pokemonType)

#
#if dualType == -1:
#    print("Single Type")
#    print(pokemonType + " weaknesses: ")
#else:
#    print("Dual Type")





#boolForType = types.find("Water")
#print(boolForType)


 

#print(pokemonType)
#print(typeVar)
