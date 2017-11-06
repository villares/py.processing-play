import csv
f = open("file.csv")
table = csv.reader(f)
for line in table:
    print line