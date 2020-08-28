import csv

with open('data/names_email.csv', 'r') as rf, \
     open('output/names_email_custom_header.csv', 'w') as wf:

     csv_reader = csv.DictReader(rf)
     orig_headers = next(csv_reader)
     csv_writer = csv.DictWriter(wf, fieldnames=orig_headers)
     desired_headers = ['fname', 'lname', 'email_id']
     csv_writer.fieldnames = desired_headers
     csv_writer.writeheader()
     csv_writer.fieldnames = orig_headers

     for line in csv_reader:
        csv_writer.writerow(line)
