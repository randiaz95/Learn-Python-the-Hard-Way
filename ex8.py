
# Get a string that is ready for formatting
formatter = "{} {} {} {}"

# Pass integers through the format method
print(formatter.format(1,2,3,4))

# Pass strings throught the format method
print(formatter.format("one", "two", "three", "four"))

# Pass booleans through the format method
print(formatter.format(True, False, False, True))

# Pass the formatting string through itself
print(formatter.format(formatter, formatter, formatter, formatter))

# Pass random text through to make a sentence
print(formatter.format(
	"Try your", 
	"Own text here", 
	"Maybe a poem", 
	"Or a song about fear"
	))