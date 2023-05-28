# @author Varun Agrawal

# Working with Dictionary
my_dict={
    "name": "John",
    "age": 24,
    "country": "India"
}

# Before Appending Value
print ("Before Adding Value")
print("my_dict ", my_dict)

for key in my_dict:
    print(key," --> ", my_dict[key])


my_dict["city"]="Delhi"

# After Appending Value
print ("After Adding Value")
print("my_dict ", my_dict)

for key in my_dict:
    print(key," --> ", my_dict[key])