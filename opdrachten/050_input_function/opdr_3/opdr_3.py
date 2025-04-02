# Opdracht 3 input functie
# Naam student: Silas Brinkman
# Groep: IT2B

objecten = []

print("Voer minimaal 5 steden in (druk na elke stad op Enter):")
for i in range(5):
    invoer = input(f"Voer stad {i+1} in: ")
    objecten.append(invoer)

extra = input("Wil je nog een stad toevoegen? (ja/nee): ")
while extra.lower() == "ja":
    invoer = input("Voer extra stad in: ")
    objecten.append(invoer)
    extra = input("Wil je nog een stad toevoegen? (ja/nee): ")

objecten.sort(reverse=True)

print("Gesorteerde lijst in omgekeerde volgorde:", objecten)