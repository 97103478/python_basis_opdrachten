# Opdracht 1 functies
# Naam student: Silas Brinkman
# Groep: IT2B

def write_to_file(bestandsnaam, tekst):
    with open(bestandsnaam, "a") as bestand:
        bestand.write(tekst + "\n")

my_tekst = "Schrijf dit maar even in een bestandje"
my_file = "test.txt"
write_to_file(my_file, my_tekst)