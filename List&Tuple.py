"""
#PYTHON LIST(Mutable)

grocery = ["Uncle Chips", "Chocolate", "pen", "gum", "pencil", 56, 25, 2.6]
print(grocery[5])  # Print or access the element in 5th index
print(grocery.index("Chocolate"))  # Print the index number of Chocolate

numbers = [2, 10, 12, 19, 20, 147, 0, 87, 96]
numbers.sort()  # Sorting numbers
print(numbers)

numbers.reverse()  # Reverse sorting of numbers
print(numbers)

print(numbers[::])  # Calculated as [0:(len of the full string):1] by default

# Max and min of numbers
print(max(numbers))
print(min(numbers))

#Append
numbers.append(9)
print(numbers)

# Remove
numbers.remove(9)
print(numbers)

# Insert numbers (index num, num to be inserted)
numbers.insert(2, 25)
print(numbers)

#Remove the last element
numbers.pop()
print(numbers)

"""

#PYTHON TUPLE (Immutable)

tp = (1, 2, 3)
print(tp)

#Interhange two numbers

a = 12
b = 16

(a,b) = (b,a)

print(a, b)
