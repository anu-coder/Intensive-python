import csv

with open('data/names.csv', 'r') as f:
    csv_reader = csv.reader(f)
    # ignoring header
    next(csv_reader)

    for line in csv_reader:
        print(line)