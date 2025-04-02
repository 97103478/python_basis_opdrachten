# Opdracht 2 berekeningen
# Naam student: Silas Brinkman
# Groep: IT2B

# Hier komt je code...

gasten = ["Paul", "Kees", "Marie", "Hilda"]

gasten.insert(0, "Silas")
print("Originele lijst:", gasten)  # ["Silas", "Paul", "Kees", "Marie", "Hilda"]

gasten.remove("Marie")
print("Na afzegging Marie:", gasten)  # ["Silas", "Paul", "Kees", "Hilda"]

kees_index = gasten.index("Kees")  # Vind de positie van Kees
gasten.insert(kees_index + 1, "George")  # Voeg George toe na Kees
print("Met George erbij:", gasten)  # ["Silas", "Paul", "Kees", "George", "Hilda"]