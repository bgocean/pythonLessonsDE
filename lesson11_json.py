import json

#Data to be writing

dictionary = {
    "name": "mattias",
    "rollno": 56,
    "cgpa": 8.6,
    "phone": 9976770500
}

# Serializing json
json_object = json.dumps(dictionary, indent=4)
print(type(json_object))
print(json_object)

print("-------------------------------------")

# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)

#reading
# Open JSON file
with open('sample.json', 'r') as openfile:
    # Reading from json file
    json_object = json.load(openfile)

print(json_object)
print(type(json_object))

