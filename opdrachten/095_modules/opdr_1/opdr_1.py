import my_modules.csv_utils as csv

csv_data = """Jan,van der,vliet, zandlaan 13, 4930 FJ, Harsen
Kees,,Marijnissen, Perenboomweg 21, 3999 GG, Plaaggeest
GRIET,van der,Pol, Harlekijnplein 33, 4952 DN, Den haag
Tara,,weeslanden, Kreakenmolenweg 3, 3900 DG, Muizegat
clarijn,,Ommezwaai, Melemoor 20, 4992 DS, Haperen
Piet,De,Vries, Stelsprong 10, 4930 DF, Harsen
Jan jaap,,Siewers, De kaapstander 20, 8251 LH, Dronten"""

with open("test.csv", "w") as f:
    f.write(csv_data)

persons = []
for line in open("test.csv", "rt"):
    lst = csv.sanitize(line)
    person = csv.create_person(lst)
    person = csv.add_fullname(person)
    persons.append(person)

csv.print_persons(persons)