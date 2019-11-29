'''
Read/write from a json file
'''

import json

with open('data/states.json', 'r') as f:
        data = json.load(f)


output_data = {'states': []}
for state in data['states']:
    l = output_data['states'] # NOTE: Ref. is maintained
    d = {k:state[k] for k in ['name', 'abbreviation']}
    l.append(d)


with open('output/states_name_abbrv.json', 'w') as f:
        json.dump(output_data, f, indent=2)