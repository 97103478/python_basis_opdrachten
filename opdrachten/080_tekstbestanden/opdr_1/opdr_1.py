# Opdracht 1 while-loops
# Naam student: Silas Brinkman
# Groep: IT2B

vragen = [
    "Wat vind je van de huidige regering?",
    "Wat vind je van de Python-lessen tot nu toe?",
    "Wat vind jij de mooiste stad van Nederland?"
]

antwoorden = []

for vraag in vragen:
    antwoord = input(vraag + " ")
    antwoorden.append(antwoord)

with open("enquete_resultaten.txt", "w") as bestand:
    for i in range(len(vragen)):
        bestand.write(f"Vraag: {vragen[i]}\n")
        bestand.write(f"Antwoord: {antwoorden[i]}\n")
        bestand.write("-" * 30 + "\n")

print("Bedankt voor het invullen! De antwoorden zijn opgeslagen in enquete_resultaten.txt")