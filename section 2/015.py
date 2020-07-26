# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# create dect 
person1 = {
    "first_name": "ahmed",
    "last_name": "samy",
    "age": 30
}
# print(type(person1), person1)

# person2 = dict("first_name": "sara", "last_name": "watson", "age": 21)
# print(type(person2), person2)

# git value 
# print(person1["first_name"])
print(person1.get("phone"))


person1["phone"] = "0000000000"
# # print(person1.get("phone"))





# # Get dict keys
# print(person.keys())

# # Get dict items
# print(person.items())

# # Copy dict
# person2 = person.copy()
# person2['city'] = 'Boston'

# # Remove item
# del(person['age'])
# person.pop('phone')

# # Clear
# person.clear()

# # Get length
# print(len(person2))




# List of dict
people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Kevin', 'age': 25}
]

print(people[1]['name'])



