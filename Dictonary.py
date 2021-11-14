# Dictionary is nothing but key value pair

d1 = {}
print(type(d1))

d2 = {"Bony": "Momo", "Akash": "Pringles", "Boni": "loves_Akash"}
print(d2["Bony"])  # Access the dictionary key
print(d2["Boni"])

d3 = {"Shreya": "English", "Akash": {"B": "Musli", "L": "Chicken"}}
print(d3["Akash"]["B"])  # Access dictionary within dictionary

# Add new key and values to existing dict
d3["Anni"] = "Mutton"
d3["Ma"] = "Kabab"
print(d3)

# Delete a dict element
del d3["Shreya"]
print(d3)

d4 = d3.copy()  # Creating a new dict d4 which contains the copy of d3
del d4["Anni"]
print(d4)
print(d3)

# Updating dict
d3.update({"Lina": "Candy"})
print(d3)

d3.update({"Lina": "Toffee"})
print(d3)

# Fetching a particular value when u know the key
print(d3.get("Lina"))

# Print the keys only
print(d2.keys())

# Print the values only
print(d2.values())

# Print the whole key , value pairs
print(d2.items())
