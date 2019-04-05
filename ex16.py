from sys import argv

script, filename, function, content = argv

for index, arg in enumerate(argv):
	if index == 1:
		script = arg
	if index == 2:
		filename = arg
	if index == 3:
		function = arg
	if index == 4:
		content = arg 

class server(filename, function):

	def __init__(self, filename, function):
		self.filename = filename
		self.function = function

	def read_file(self):
		print("READING FILE")
		file = open(self.filename)
		print(self.filename)
	    print(file.read())
	    file.close()

	def write_file(self):
		print("WRITING FILE")
		file = open(self.filename, 'w')
		file.write(self.content)
		file.close()

	def delete_file(self):
		print("DELETING FILE")
		file = open(self.filename, 'w')
		file.truncate()
		file.close()

	def create_file(self):
		print("CREATING FILE")
		file = open(self.filename, 'w')
		file.write("")
		file.close()


instance = server(filename, function)

if operation.function == 'read':
	operation.read_file()

if operation.function == 'write':
	operation.write_file(content)

if operation.function == 'delete':
	operation.delete_file()

if operation.function == 'create':
	operation.create_file()