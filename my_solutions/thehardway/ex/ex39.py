# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print ('-' * 10)
print ("NY state has: ", cities['NY'])
print ("OR state has: ", cities['OR'])

# print out some states
print ('-' * 10)
print ("Michigan's abreviation is: ", states['Michigan'])
print ("Florida's abreviation is: ", states['Florida'])

# do it by using the state then cities dict
print ('-' * 10)
print ("Michigan has:", cities[states['Michigan']])
print ("Florida has: ", cities[states['Florida']])

# print every state abbreviation
print ('-' * 10)
for state, abbrev in states.items():
    print ("%s is abbreviated %s" % (state, abbrev))

# now both at the same time
print ('-' * 10)
for state, abbrev in states.items():
    print ("%s state is abbreviated %s and has city %s" % (
        state, abbrev, cities[abbrev]))

print ('-' * 10)
# safely gat an abbreviation by state tjat might not be there
state = states.get('Texas')

if not state:
    print ("Sorry, no Texas.")

# get a city with a deaful value
city = cities.get('CA', 'Does not exist')
print ("The city for the state 'TX' is: %s" % city)