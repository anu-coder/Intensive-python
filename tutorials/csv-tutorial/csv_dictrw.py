import csv

with open('data/names_email.csv', 'r') as rf, \
     open('output/fname_email.tsv', 'w') as wf:

    csv_reader = csv.DictReader(rf)
    fieldnames = ['email', 'first_name'] # choose what to write + order
    csv_writer = csv.DictWriter(wf, fieldnames=fieldnames, delimiter='\t')

    csv_writer.writeheader()

    next(csv_reader)# skip header
    for line in csv_reader:
        del line['last_name'] # NOTE: This is req to match fieldnames
        csv_writer.writerow(line)
