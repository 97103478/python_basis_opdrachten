# Opdracht 2 berekeningen
# Naam student: Silas Brinkman
# Groep: IT2B

# Hier komt je code...

c = -12
f = 102

c2 = 62.2
f2 = 96

c_to_f = (c * 9/5) + 32 #celsius naar fahrenheit
f_to_c = (f -32) * 5/9 # fahrenheit naar celsius

c2_to_f = (c2 * 9/5) + 32  # Celsius naar Fahrenheit
f2_to_c = (f2 - 32) * 5/9  # Fahrenheit naar Celsius

print(f"{c} graden Celsius is gelijk aan {c_to_f:.1f} graden Fahrenheit")
print(f"{f} graden Fahrenheit is gelijk aan {f_to_c:.1f} graden Celsius")

print(f"{c2} graden Celsius is gelijk aan {c2_to_f:.1f} graden Fahrenheit")
print(f"{f2} graden Fahrenheit is gelijk aan {f2_to_c:.1f} graden Celsius")