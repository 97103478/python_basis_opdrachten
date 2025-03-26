# Opdracht 2 lists
# Naam student: Silas Brinkman
# Groep: IT2B


rivier_info = {
    "rijn": ["nederland", "duitsland", "Frankrijk"],
    "maas": ["nederland", "belgië", "duitsland"],
    "nijl": ["egypte", "soedan", "oeganda"]
}

rivieren = list(rivier_info.keys())

rivier1 = rivieren[0].capitalize()  # "Rijn"
land1 = rivier_info[rivieren[0]][1].capitalize()  # "Duitsland"
print(f"De rivier {rivier1} stroomt onder andere door {land1}")

rivier2 = rivieren[1].capitalize()  # "Maas"
land2 = rivier_info[rivieren[1]][0].capitalize()  # "Nederland"
print(f"De rivier {rivier2} stroomt onder andere door {land2}")

rivier3 = rivieren[2].capitalize()  # "Nijl"
land3 = rivier_info[rivieren[2]][2].capitalize()  # "Oeganda"
print(f"De rivier {rivier3} stroomt onder andere door {land3}")