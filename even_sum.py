# Arthur Musoke
# Lab 3 - Even Number Sum

# Using a for loop
total_for = 0

for number in range(1, 51):
    if number % 2 == 0:
        total_for += number

print("For Loop Result:")
print("The sum of even numbers from 1 to 50 is", total_for)

# Using a while loop
total_while = 0
number = 1

while number <= 50:
    if number % 2 == 0:
        total_while += number
    number += 1

print("\nWhile Loop Result:")
print("The sum of even numbers from 1 to 50 is", total_while)

# Both loops produce the same result.
# I think the for loop is easier to read because it uses fewer lines of code.
