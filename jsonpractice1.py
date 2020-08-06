import json
data = '''{
    "name": "Chuck",
    "phone": {
        "type": "intl",
        "number": "+1 734 303 4456"
    },
    "email": {
        "hide":"yes"
    }
}'''

loadup = json.loads(data)
print ('Name:',loadup['name'])
print ('Hide:',loadup['email']['hide'])
print ('Phone type:',loadup['phone']['type'])
print ('Phone:',loadup['phone']['number'])