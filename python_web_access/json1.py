import json

data = '''{
"name": "Arya",
"phone": {
"type": "intl",
"number": "976 653 9098"
},
"email": {
"hide" : "yes" 
}
}'''

info = json.loads(data)
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])
