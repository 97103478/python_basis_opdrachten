# Opdracht 1 lists
# Naam student: Silas Brinkman
# Groep: IT2B

# Maak een lege lijst
personen_lijst = []

# Maak vier dictionaries voor personen
persoon1 = {"id": 0, "voornaam": "Jan", "achternaam": "Jansen"}
persoon2 = {"id": 1, "voornaam": "Piet", "achternaam": "Pietersen"}
persoon3 = {"id": 2, "voornaam": "Klaas", "achternaam": "Klaassen"}
persoon4 = {"id": 3, "voornaam": "Anna", "achternaam": "Annasen"}

# Voeg de dictionaries toe aan de lijst
personen_lijst.append(persoon1)
personen_lijst.append(persoon2)
personen_lijst.append(persoon3)
personen_lijst.append(persoon4)

# Print de volledige naam van de tweede persoon
print(personen_lijst[1]["voornaam"], personen_lijst[1]["achternaam"])