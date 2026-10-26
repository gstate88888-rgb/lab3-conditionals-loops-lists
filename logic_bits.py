# Arthur Musoke
# Lab 3 - Logic and Bitwise Operators

# Logical operators
a = bool(int(input("Enter 1 for True or 0 for False: ")))
b = bool(int(input("Enter 1 for True or 0 for False: ")))

print("\nLogical Operations")
print("AND:", a and b)
print("OR:", a or b)
print("NOT A:", not a)

# Bitwise operators
x = 5
y = 3

print("\nBitwise Operations")
print("x =", x, "=", bin(x))
print("y =", y, "=", bin(y))

print("x & y =", bin(x & y))
print("x | y =", bin(x | y))
print("x ^ y =", bin(x ^ y))
print("~x =", bin(~x))
print("x << 1 =", bin(x << 1))
print("x >> 1 =", bin(x >> 1))
