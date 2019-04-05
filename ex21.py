# Functions with math!
def add(a, b):
    return a+b


def subtract(a, b):
    return a-b


def multiply(a, b):
    return a*b


def divide(a, b):
    return a/b

print("Let's just do math with just functions.")

age = add(20, 2)
height = subtract(8, 2)
weight = multiply(2, 100)
iq = divide(200, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}.")

# A puzzle for extra credit, type it in anyways
print("Here is a puzzle")
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")
# Nope... lolz
