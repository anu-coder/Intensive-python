'''
Read and dump json strings
'''

import json

s = '''
{
  "employees": [
    {
      "name": "Shyam",
      "email": "shyamjaiswal@gmail.com",
      "phone": "998877665"
    },
    {
      "name": "Bob",
      "email": "bob32@gmail.com",
      "phone": "998877664"
    },
    {
      "name": "Jai",
      "email": "jai87@gmail.com",
      "phone": "998877663"
    }
  ]
}
'''

data = json.loads(s)
for emp in data['employees']:
    del emp['email'] # NOTE: This will delete from data too (since emp is a ref)

new_s = json.dumps(data, indent=2, sort_keys=True)
print(new_s)