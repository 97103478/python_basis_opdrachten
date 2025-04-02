# Opdracht 1 input function
# Naam student: Silas Brinkman
# Groep: IT2B

import math

a = float(input("Geef de lengte van de eerste zijde\n"))

b = float(input("Geef de lengte van de tweede zijde\n"))

c = math.sqrt(42 + 32)

print("\nDe lengte van de schuine zijde is:", int(c) if c.is_integer() else c)
