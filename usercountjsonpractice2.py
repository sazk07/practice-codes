import json
data = '''[
    { "id" : "001", "x" : "2", "Name" : "Chuck"},
    { "id": "009", "x" : "7", "Name" : "Chuck2" }
]'''

loadup = json.loads(data)
print ('User count:',len(loadup))
for eachitem in loadup:
    print ('Name:',eachitem['Name'])
    print ('ID:',eachitem['id'])
    print ('Attribute:',eachitem['x'])