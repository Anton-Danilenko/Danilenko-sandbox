import json
str_json = """
{
"response": 
 {
    "peoples": 
    [   
        {
        "firstName": "Иван",
        "lastName": "Иванов",
        "address": "Московское ш., 101, кв.101",
        "phoneNumbers": "812 123-1234"
        },
        {
        "firstName": "Петр",
        "lastName": "Петров",
        "address": "Советская, 150",
        "phoneNumbers": "812 111-1111"
        }
    ]
 }
}
"""
#print (type(str_json))

data = json.loads(str_json)
#print (type(data))

for peoples in data['response']['peoples']:
    print(peoples['lastName'], peoples['firstName'],peoples['phoneNumbers'])
