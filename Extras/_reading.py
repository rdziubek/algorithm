with open('../in/galerie_przyklad.txt') as file:
    rows = [row.strip().split() for row in file.readlines() if row.strip()]

for row in rows:
    kraj = row[0]
    miasto = row[1]
    wymiary = row[2:]
