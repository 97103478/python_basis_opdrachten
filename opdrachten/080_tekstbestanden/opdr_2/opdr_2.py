# Opdracht 2 tekstbestanden
# Naam student: Silas Brinkman
# Groep: IT2B

import random

geheim_getal = random.randint(1, 100)
aantal_pogingen = 0


while True:

    print("Raad mijn geheime getal")
    gok = int(input())
    aantal_pogingen += 1
    

    if gok < geheim_getal:
        print("hoger")
    elif gok > geheim_getal:
        print("lager")
    else:
        print(f"Je hebt het getal geraden het is {geheim_getal}!")
        print(f"Je hebt het in {aantal_pogingen} keer gedaan")
        break