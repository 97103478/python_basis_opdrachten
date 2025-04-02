# Opdracht 3 Tekst opslaan
# Naam student: Silas Brinkman
# Groep: IT2B

def encrypt(tekst):
    resultaat = ""
    for letter in tekst:
        if letter.isalpha():
            is_hoofdletter23 = letter.isupper()
            code = ord(letter.lower())
            verschoven = code + 5
            
            if verschoven > ord('z'):
                verschoven = verschoven - 26
                
            nieuwe_letter = chr(verschoven)
            if is_hoofdletter23:
                nieuwe_letter = nieuwe_letter.upper()
            resultaat += nieuwe_letter
        else:
            resultaat += letter
    return resultaat

invoer = input("Geef de tekst die wilt encrypten..\n")

geencrypteerd = encrypt(invoer)
print(geencrypteerd)

