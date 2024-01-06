# Basics of python programing

## Good first step
print('hello world')


## In python, we can use both '' or "" on our code
## There is only one tip: once you chose one, use it throughout the code 


## Data types (tells how much memory to allocate)
type(10) # Int
type(10.55) # Float
type('10') # Str
type(True) # Bool


## Data types Conversions
int()
float()
str()
bool()

## Constants and variables
CONSTANT_VALUE= 'constante' # Definition on snake case and in upper case
variable_value= 'variable' # Definition on snake case and in lower case

## Input and output functions
### Inputs with description
name= input('Write your name:') # Recieve, at the end of the phrase, a string
age= input('Write your age:') # Recieve, at the end of the phrase, a string

### Outputs
print(name, age, end='\n') # Print each inputed string and break line at the end
print(name, age, sep='\n', end='\n') # Print each inputed string separated with breakline and then 
###break line at the end