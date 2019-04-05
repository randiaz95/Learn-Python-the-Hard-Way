# This one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}.")


# *args is pointless in the previous function argument
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}.")


# This takes one argument
def print_one(arg):
    print(f"arg: {arg}.")


# This one takes no arguments
def print_none():
    print("I got nothing")


print_two("Randy", "Diaz")
print_two_again("Randy", "Diaz")
print_one("First!")
print_none()
