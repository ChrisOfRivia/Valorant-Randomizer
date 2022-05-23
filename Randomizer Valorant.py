import random

valorant_agents = ['Astra', 'Jett', 'KA/YO', 'Phoenix', 'Sage', 'Sova', 'Breach', 'Cypher',
                   'Fade', 'Killjoy', 'Neon', 'Omen', 'Raze', 'Reyna', 'Skye', 'Viper',
                   'Yoru', 'Brimmstone', 'Chamber']

valorant_weapons_start = ['Classic', 'Shorty', 'Frenzy', 'Ghost', 'Sheriff']
valorant_weapons_affordable = ['Classic', 'Shorty', 'Frenzy', 'Ghost', 'Sheriff', 'Stinger',
                               'Spectre', 'Bucky', 'Judge', 'Bulldog', 'Guardian', 'Phantom',
                               'Vandal', 'Marshal', 'Ares']

random_agent = random.choice(valorant_agents)
random_start = random.choice(valorant_weapons_start)
random_until_the_end = random.choice(valorant_weapons_affordable)

print("Welcome my Valorant randomizer!")
weapon = input("Would you like a random weapon? Y/N: ")
if weapon.upper() == "Y":
    print(f""" \n You will be playing:  {random_agent}  
 pistol round you will be playing  {random_start} 
 and until the end of the game you will play  {random_until_the_end}  
 GL HF!""")
else:
    print(f""" \n You will be playing:  {random_agent}
 GL HF!""")

