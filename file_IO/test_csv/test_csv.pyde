import csv

with open("file.csv") as f:
    table = list(csv.reader(f))

for line in table:
    print(line)
