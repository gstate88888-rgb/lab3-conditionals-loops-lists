# Arthur Musoke
# Lab 3 - Bubble Sort Demo

numbers = [64, 25, 12, 22, 11]

print("Original List:")
print(numbers)

for i in range(len(numbers)):

    # Compare neighboring values
    for j in range(0, len(numbers) - i - 1):

        # Swap values if they are out of order
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    print(f"Pass {i + 1}: {numbers}")

print("\nFinal Sorted List:")
print(numbers)
