from sys import argv
from os.path import exists
from os import makedirs

for index, arg in enumerate(argv):
    print(index, arg)
    if index == 0:
        filename = arg
    if index == 1:
        function = arg
    if index == 2:
        description = arg


class server(object):

    def __init__(self, content, command):
        if not exists("data"):
            makedirs("data")
        self.filename, *data = content.split("-")
        self.filename = 'data\\'+self.filename
        self.data = ''.join(data)
        self.function = command

    def read_file(self):
        print("READING FILE")
        file = open(self.filename)
        print(file.read())
        file.close()
        return None

    def write_file(self):
        print("WRITING FILE")
        file = open(self.filename, 'w')
        file.write(self.data)
        file.close()
        return None

    def delete_file(self):
        print("DELETING FILE")
        file = open(self.filename, 'w')
        file.truncate()
        file.close()
        return None

    def create_file(self):
        print("CREATING FILE")
        if exists(self.filename):
            print("File already exists.")
            return None
        else:
            file = open(self.filename, 'w+')
            file.write("")
            file.close()
            return None


operation = server(content=description, command=function)

if operation.function == 'read':
    operation.read_file()

if operation.function == 'write':
    operation.write_file()

if operation.function == 'delete':
    operation.delete_file()

if operation.function == 'create':
    operation.create_file()
