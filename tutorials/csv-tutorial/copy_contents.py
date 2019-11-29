import csv

with open('data/names_email.csv', 'r') as rf, \
     open('output/fullnames.tsv', 'w') as wf:

     csv_reader = csv.reader(rf)
     csv_writer = csv.writer(wf, delimiter='\t')

     for fname, lname, email in csv_reader:
        csv_writer.writerow([fname, lname]) # leaving out email