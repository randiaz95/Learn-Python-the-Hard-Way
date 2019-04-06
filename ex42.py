## Animal is an object (yes, sort of confusing)
class Animal(object):
	pass

## A dog is an animal
class Dog(Animal):

	def __init__(self, name):
		## Each dog has a name
		self.name = name

## A cat is an animal
class Cat(Animal):

	def __init__(self, name):
		## Each cat has a name too.
		self.name = name

## People are objects
class Person(object):

	def __init__(self, name):
		## Each person has a name as well.
		self.name = name
		## Person may have a pet of some kind.
		self.pet = None

## An employee is a person.
class Employee(Person):

	def __init__(self, name, salary):
		## Employees are human thus have names.
		super(Employee, self).__init__(name)
		## Employees have a salary.
		self.salary = salary

# Fish is an object
class Fish(object):
	pass

# Salmon is a fish.
class Salmon(Fish):
	pass

# Halibut is a fish.
class Halibut(Fish):
	pass

## Rover is a dog.
rover = Dog("Rover")

## Satan is a cat
satan = Cat("Satan")

## Mary is a person
mary = Person("Mary")

## Mary's pet is satan and satan is a cat
mary.pet = satan

## Frank is an employee that has 120k salary
frank = Employee("Frank", 120000)

# Frank's pet is rover
frank.pet = rover

## Flipper is a fish
flipper = Fish()

## crouse is a salmon
crouse = Salmon()

## Harry is a halibut
harry = Halibut()
