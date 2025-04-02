# Opdracht 4 Tekst opslaan
# Naam student: Silas Brinkman
# Groep: IT2B

vragen = [
    "Wat is je voornaam?",
    "Wat is je achternaam?",
    "Wat neem je mee aan drank?",
    "Wat neem je mee om te eten?"
]

feestganger = {}

for i, vraag in enumerate(vragen, 1): 
    antwoord = input(f"{i}. {vraag} \n")
    if i == 1:
        feestganger["voornaam"] = antwoord
    elif i == 2:
        feestganger["achternaam"] = antwoord
    elif i == 3:
        feestganger["drank"] = antwoord
    else:
        feestganger["eten"] = antwoord

with open("party_gasten.txt", "a") as bestand:
    bestand.write("----\n")
    for key, value in feestganger.items():
        bestand.write(f"{key}: {value}\n")
    bestand.write("\n")

print("\nBedankt voor het invullen!")
print("See you at the party.")