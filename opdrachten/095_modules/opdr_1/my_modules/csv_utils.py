def sanitize(line):
    """Clean and split a CSV line into a list."""
    return [item.strip() for item in line.strip().split(",")]

def create_person(lst):
    """Create a person dictionary from a list of CSV values."""
    return {
        "first_name": lst[0],
        "middle_name": lst[1],
        "last_name": lst[2],
        "address": lst[3],
        "zip_code": lst[4],
        "city": lst[5]
    }

def add_fullname(person):
    """Add a formatted full name to the person dictionary."""
    first = person["first_name"].capitalize()
    middle = person["middle_name"].capitalize() if person["middle_name"] else ""
    last = person["last_name"].capitalize()
    full_name = f"{first} {middle} {last}".replace("  ", " ").strip()
    person["full_name"] = full_name
    return person

def print_persons(persons):
    """Print the list of persons and the total count."""
    for person in persons:
        print(f"Name: {person['full_name']}, Address: {person['address']}, {person['zip_code']} {person['city']}")
    print(f"\nTotal persons: {len(persons)}")