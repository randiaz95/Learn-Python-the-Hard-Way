from sys import argv
from os.path import exists

script, from_file, to_file = argv
print(f"Copying from {from_file} to {to_file}.")

# We could do these two on one line, how?
"""
in_file = open(from_file)
indata = in_file.read()

@Doing this below is bad because we need to close the file
in_data = open(from_file).read()

@Do this instead, but not pep8 compliant so keep on two lines
in_file = open(from_file);in_data = in_file.read();

Also to open a file, process its contents,
and make sure to close it, you can simply do:

with open("x.txt") as f:
    data = f.read()
    do something with data

^ The above closes the object on it's own.

with open('a', 'w') as a, open('b', 'w') as b:
    do_something()

"""

in_file = open(from_file)
in_data = in_file.read()

print(f"The input file is {len(in_data)} bytes",
      "long.\nDoes the output file exist? {exists(to_file)}.")
input("Ready, hit RETURN to continue, CTRL-C to abort.")

new_file = open(to_file, 'w')
out_file = new_file.write(in_data)

print("Alright, all done.")
map(lambda x: x.close(), [new_file, in_file])
