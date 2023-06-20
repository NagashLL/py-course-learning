import json
data = '''{
    "name" : "Chuck",
    "phone" : {
        "type" : "int1",
        "number" : "+1 734 303 4456"
    },
    "email" : {
        "hide" : "yes"
    }
}
'''

info = json.loads(data)
print ('Name:', info["name"])
print ('Phone:',info["phone"]["number"])
print ('Attribute:', info["email"]["hide"])


input = '''[
    { "id" : "001",
      "x"  : "2",
      "name" : "Adrian"
    },
    { "id" : "002",
      "x"  : "6",
      "name" : "Brian"
    }
]'''

job = json.loads(input)
print('Name', job[0]['name'])
                #we can use the [0] to do the first item in the array, otherwise it will output an error   

for item in job:
    print('Name:',item["name"])
    print('Id:', item["id"])
    print('x:',item["x"])
    print('Name', item["name"])
    #simple structure for retrieving items