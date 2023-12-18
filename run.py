import csv

names = []

with open("sheet.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        name = row["name"].strip().upper()
        if not row["name"] in names:
            names.append(name)

for name in names:
    print(name)