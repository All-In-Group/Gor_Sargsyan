import json

#Question 1
'''
Question 1: Convert the following data into JSON format

'''

data = {"key1" : "value1", "key2" : "value2"}
print(f"Question 1 solution: {json.dumps(data)}\n")

#Question 2
'''
Question 2: Access the value of key2 from the following JSON

'''
sampleJson = """{"key1": "value1", "key2": "value2"}"""
dict1 = json.loads(sampleJson)
print(f"Question 2 solution: {dict1['key2']}\n")

#Question 3

'''
Question 3: PrettyPrint following JSON data
PrettyPrint following JSON data with indent level 2 and key-value separators should be (",", " = ").
sampleJson = {"key1": "value1", "key2": "value2"}

'''
sampleJson = {"key1": "value1", "key2": "value2"}
file = json.dumps(sampleJson,indent=2,separators=(",", " = "))
print(f"Quiestion 3 solution: {file}\n")

#Question 4

'''
Question 4: Sort JSON keys in Python and write it into a file
Sort following JSON data alphabetical order of keys

'''

sampleJson = {"id" : 1, "name" : "value2", "age" : 29}
file = json.dumps(sampleJson,sort_keys=True)
print(f"Question 4 solution: {file}\n")

#Question 5
'''
Question 5: Access the nested key ‘salary’ from the following JSON

'''
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

file = json.loads(sampleJson)
print(f'Question 5 solution: {file["company"]["employee"]["payble"]["salary"]}\n')

#Question 6
'''
Question 6: Convert the following Vehicle Object into JSON

'''
class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price
    

vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)
dict1 = vars(vehicle)
filejson = f"'{json.dumps(dict1,indent=4)}'"
# vehicle_json = json.dumps(vehicle,)
print(f"Question 6 solution: {filejson}\n")

#Question 7
'''
Question 7: Convert the following JSON into Vehicle Object

{ "name": "Toyota Rav4", "engine": "2.5L", "price": 32000 }

For example, we should able to access Vehicle Object using the dot operator like this.

vehicleObj.name, vehicleObj.engine, vehicleObj.price
'''
def decoder(obj):
    return Vehicle(obj["name"],obj["engine"],obj["price"])

vehicleObj = json.loads('{"name": "Toyota Rav4","engine": "2.5L","price": 32000}',object_hook=decoder)
print(f"Question 7 solution is {vehicleObj.engine},{vehicleObj.name},{vehicleObj.price}\n")

#Question 8
file = """{ "company":{ "employee":{ "name":"emma", "payble":{ "salary":7000 ,         "bonus":8000}}}}"""
file_false = """{ "company":{ "employee":{ "name":"emma", "payble":{ "salary":7000  "bonus":8000}}}}"""

#echo /jsontext/ | python -m json.tool 
def valid_or_not(jsonfile):
    try:
        json.loads(jsonfile)
    except ValueError:
        return False
    return True

isvalid = valid_or_not(file)
isvalid_false = valid_or_not(file_false)

print(f"Question 8 solution : json file is {isvalid}")
print(f"Question 8 solution : json file is {isvalid_false}\n")


#Question 8

'''
Question 9: Parse the following JSON to get all the values of a key ‘name’ within an array
'''
jsonfile = """[ 
   { 
      "id":1,
      "name":"name1",
      "color":[ 
         "red",
         "green"
      ]
   },
   { 
      "id":2,
      "name":"name2",
      "color":[ 
         "pink",
         "yellow"
      ]
   }
]"""

file = json.loads(jsonfile)
listof_item= [item["name"] for item in file]

print(f"Question 9 solution: {listof_item}")


#Question 9
