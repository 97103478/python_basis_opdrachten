# Opdracht 1 functies
# Naam student: Silas Brinkman
# Groep: IT2B

def kilometers_naar_miles(kilometers):
    return kilometers / 1.609344

def miles_naar_kilometers(miles):
    return miles * 1.609344

kilometers = 1223
miles = 867

miles_resultaat = kilometers_naar_miles(kilometers)
km_resultaat = miles_naar_kilometers(miles)

print(f"{kilometers} kilometers = {miles_resultaat} miles")
print(f"{miles} miles = {km_resultaat} kilometers")