# if, elif and else logic

ALLOWED_AGE = 18
SPECIAL_AGE = 19
ALMOST_SPECIAL_AGE = 20


your_age = int(input('Insert your age: '))
if your_age >= ALLOWED_AGE: # If TRUE, continues
    print('Allowed')
if your_age == SPECIAL_AGE: # If TRUE, continues
    print('You are special')
elif your_age == ALMOST_SPECIAL_AGE: # If all above are FALSE and this one is TRUE, this one
    print('You are almost special')
else:
    print('not allowed')

# So, if your_age = 19, We'll get a 2 messages output
# And if your_age = 17, We'll get a single message output (because all above answers are false)