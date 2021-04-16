import csv
with open('NHLEExport.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(dict(row)["Link"])
