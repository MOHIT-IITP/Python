# Return a sorted copy of the list x
x.sorted(x) # Returns [1, 2, 3]

# Sort the list in-place (replaces x)
x.sort() # Returns None

# Reverse the order of elements in x
reversed(x) # Returns [2, 3, 1]

# Reverse the item in the list 
x.reversed() # Returns None

# Count the number of element 2 in the list
x.count(2)

# Define the list 
x = ['a', 'b', 'c', 'd', 'e']

# Select the 0th element in the list
x[0] # 'a'

# Select the last element in the list
x[-1] # 'e'

# Select 1st (inclusive) to 3rd (exclusive)
x[1:3] # ['b', 'c']

# Select the 2nd to the end
x[2:] # ['c', 'd', 'e']

# Select 0th to 3rd (exclusive)
x[:3] # ['a', 'b', 'c']

# Define the list x and y  
x = [1, 3, 6] 
y = [10, 15, 21]

# Concatenate lists with +
x + y # [1, 3, 6, 10, 15, 21]

# Repeat list n times with *
3 * x # [1, 3, 6, 1, 3, 6, 1, 3, 6]

# Define the dictionary
a = {'a': 1, 'b': 2, 'c': 3}

# Get the keys
x.keys() # dict_keys(['a', 'b', 'c'])

# Get  the values
x.values() # dict_values([1, 2, 3])

# Get a value from a dictionary by specifying the key
x['a'] # 1


# Convert a python list to a NumPy array
np.array([1, 2, 3]) # array([1, 2, 3])

# Return a sequence from start (inclusive) to end (exclusive)
np.arange(1,5) # array([1, 2, 3, 4])

# Return a stepped sequence from start (inclusive) to end (exclusive)
np.arange(1,5,2) # array([1, 3])

# Repeat values n times
np.repeat([1, 3, 6], 3) # array([1, 1, 1, 3, 3, 3, 6, 6, 6])

# Repeat values n times
np.tile([1, 3, 6], 3) # array([1, 3, 6, 1, 3, 6, 1, 3, 6])


# Calculate logarithm of an array
np.log(x) 
# Calculate exponential of an array
np.exp(x)
# Get maximum value of an array
np.max(x)
# Get minimum value of an array
np.min(x)
# Calculate sum of an array
np.sum(x)
# Calculate mean of an array
np.mean(x)
# Calculate q-th quantile of an array x
np.quantile(x, q)
# Round an array to n decimal places
np.round(x, n)
# Calculate variance of an array
np.var(x)
# Calculate standard deviation of an array
np.std(x)

# Create a string variable with single or double quotes
"DataCamp"

# Embed a quote in string with the escape character \
"He said, \"DataCamp\""

# Create multi-line strings with triple quotes
"""
A Frame of Data
Tidy, Mine, Analyze It
Now You Have Meaning
Citation: https://mdsr-book.github.io/haikus.html
"""

# Get the character at a specific position
str[0] 

# Get a substring from starting to ending index (exclusive)
str[0:2]


# Concatenate strings with +
"Data" + "Framed" # 'DataFramed'

# Repeat strings with *
3 * "data " # 'data data data '

# Split a string on a delimiter
"beekeepers".split("e") # ['b', '', 'k', '', 'p', 'rs']


#STRING

# Create a string named str
str = "Jack and Jill"

# Convert a string to uppercase
str.upper() # 'JACK AND JILL'

# Convert a string to lowercase
str.lower() # 'jack and jill'

# Convert a string to title case
str.title() # 'Jack And Jill' 

# Replaces matches of a substring with another
str.replace("J", "P") # 'Pack and Pill'


