# opdr_1.py
import personen  # Importeer je zelfgemaakte module (pas de naam aan als nodig)

def filter(persoon, filterveld, filter):
    """
    Filtert de lijst van personen op basis van een veld en een beginstring.
    
    Args:
        persoon: Lijst van dictionaries met persooninformatie
        filterveld: Het veld waarop gefilterd wordt (bijv. 'voornaam', 'plaats')
        filter: De beginstring om op te filteren (bijv. 'ja', 'd')
    
    Prints:
        De gefilterde personen in het formaat 'voornaam achternaam'.
    """
    for p in persoon:
        if filterveld in p and p[filterveld].lower().startswith(filter.lower()):
            print(f"{p['voornaam']} {p['achternaam']}")

# Test de filterfunctie
if __name__ == "__main__":
    # Test 1: Filter op voornaam met 'ja'
    print("Filter op voornaam met 'ja':")
    filter(personen.personen, "voornaam", "ja")
    
    # Test 2: Filter op voornaam met 'Pie'
    print("\nFilter op voornaam met 'Pie':")
    filter(personen.personen, "voornaam", "Pie")
    
    # Test 3: Filter op plaats met 'd'
    print("\nFilter op plaats met 'd':")
    filter(personen.personen, "plaats", "d")