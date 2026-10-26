# Arthur Musoke
# Lab 3 - List Operations

# Create a list
numbers = [12, 5, 20, 8, 15]

print("Original List:")
print(numbers)

# Sort without modifying original list
print("\nSorted List Using sorted():")
print(sorted(numbers))

# Sort original list
numbers.sort()
print("\nList After .sort():")
print(numbers)

# Add a new number
numbers.append(25)
print("\nAfter Appending 25:")
print(numbers)

# Remove a number
numbers.remove(8)
print("\nAfter Removing 8:")
print(numbers)

# Reverse list
numbers.reverse()
print("\nReversed List:")
print(numbers)
