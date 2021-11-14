mystr = "shreya is awesome"
print(mystr.isalpha())  # Neither alpha not numeric so false
print(mystr.isalnum())  # Spaces are present so string is not alphanumeric
print(mystr.endswith("awesome"))  # String ends with awesome so true
print(mystr.endswith("awee"))
print(mystr.count("o"))  # Counts the no. of b
print(mystr.count("b"))  # Counts the no. of b
print(mystr.capitalize())  # Capitalizes the first letter
print(mystr.find("is")) # Output the index number from where the string is starting . The index starts from 0.
print(mystr.lower()) # Prints the string in lower case
print(mystr.upper()) # Prints the string in upper case
print(mystr.replace("is", "are")) # Replace strings
