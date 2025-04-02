# Opdracht 1 functies
# Naam student: Silas Brinkman
# Groep: IT2B

import math

def kubus_vol(zijde):
    volume = zijde ** 3
    print(f"De inhoud van deze kubus is: {volume}")
    return volume

def bol_vol(straal):
    volume = (4/3) * math.pi * (straal ** 3)
    print(f"De inhoud van deze bol is: {volume}")
    return volume

volume_kubus = kubus_vol(5)
volume_bol = bol_vol(4)