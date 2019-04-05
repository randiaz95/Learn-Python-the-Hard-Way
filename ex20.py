from sys import argv

script, input_file = argv

# Would be cool to make a parent object or some architecture 
# that has all these functions already.
def print_all(f):
    print(f.read())


def rewind(f):
    # Seek starts the file object back at the byte you give it.
    f.seek(0)
    # If you put 0 then it starts at the 0th byte.


def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

print("First, let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)
current_line += 1
print_a_line(current_line, current_file)
current_line += 1
print_a_line(current_line, current_file)
