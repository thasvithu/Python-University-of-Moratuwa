"""
--- DICTIONARY ---
Ordered
Mutable => Value can be change
Indexed
Unique
"""

#Creating an empty dictionary
my_first_dict = dict()
print(my_first_dict)

#Using curly braces to initialize a dictionary
scores = {"Vithu" : 89, "Nila" : 85, "Baby" : 99}
print(scores)
print(scores["Vithu"])
print(scores.get("Nila"))


#Adding an element
scores["Test"] = 90
print(scores)

#Updating an element
scores["Nila"] = 59
print(scores)

#Remove an element
scores.pop("Test")
print(scores)

#Removing all elemnts
scores.clear()
print(scores)

#Get the list of all keys
scores = {"Vithu" : 89, "Nila" : 85, "Baby" : 99}
all_keys = list(scores.keys())
print(all_keys)

#Get the list of all values
all_values = list(scores.values())
print(all_values)