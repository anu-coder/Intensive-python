'''
Parse a csv file and write the contents to an html unorderd list
'''
import csv

html_output = ''
names = []

with open('data/patrons.csv', 'r') as f:
    csv_data = csv.DictReader(f)
    # NOTE: No need to skip headers with DictReader
    next(csv_data) # skipping description lines

    for line in csv_data:
        firstName = line.get('FirstName')
        if firstName == 'No Reward':
            break

        lastName = line.get('LastName')

        names.append(f'{firstName} {lastName}')



html_output += f'<p> There are currenly {len(names)} public contributors. </p>'
html_output += '\n<ul>'
for name in names:
    html_output += f'\n\t<li>{name}</li>'

html_output += '\n</ul>'

with open('output/names.html', 'w') as f:
    f.write(html_output)