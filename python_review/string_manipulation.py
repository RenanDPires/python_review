TEST_STRING= ' PyTHoN '

# All string upper
print(TEST_STRING.upper())

# All string lower
print(TEST_STRING.lower())

# Only first letter upper
print(TEST_STRING.title())

# Cleaning all spaces
print(TEST_STRING.strip())

# Cleaning left spaces
print(TEST_STRING.lstrip())

# Cleaning right spaces
print(TEST_STRING.rstrip())


TEST_STRING_2 = 'python'

# Center string with special characteres around
print(TEST_STRING_2.center(20,'_')) # Number of characteres, special around

# Character between each letter
print('_'.join(TEST_STRING_2)) # Number of characteres, special around

# A string is a list of characteres, so we can work with as a list
# Backward
print(TEST_STRING_2[::-1])

# All characters, except the last
print(TEST_STRING_2[:-1])

# All characters, except the first
print(TEST_STRING_2[1:])

# Third character
print(TEST_STRING_2[2]) # Starts on 0, don't forget

# Block string with 'f word'
print(f'''Here
      is 
      a big
      string with a little part of test string 2 at the end:\n\t{TEST_STRING_2[2]}''')