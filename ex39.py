# Create a mapping of state to abbreviation.
states = {'Oregon': 'OR',
		  'Florida': 'FL',
		  'California': 'CA',
		  'New York': 'NY',
		  'Michigan': 'MI'
		  }

# Create a basic set of states and some cities in them.
cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
}

# Add some more cities.
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# Print out some cities.
print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

# Print some states.
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# Print cities with the states dictionary.
print('-' * 10)
print("Michigan's abbreviation is: ", cities[states['Michigan']])
print("Florida's abbreviation is: ", cities[states['Florida']])

# Print every state abbreviation.
print('-' * 10)
for i, v in states.items():
	print(i, v)

# Now do both at the same time
print('-' * 10)
for abbrev, city in list(cities.items()):
	print(f"{abbrev} ")