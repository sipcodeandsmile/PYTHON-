#functions is essentially a collection of code performing specific tasks
#you can always recall a function once you've set it

#to create a function saying Hi
#to write a function you need the keyword def to let python know you want to use a function
def hello() : #lets python know all the code coming after this line belongs in the function, hence we have to indent
    print("Hello Riri")


#to execute the function, it needs to be called, because the code inside the function can't be executed less you specify that it has to be exexuted
#to do so, you need to call the function by typing the function name, you can call a function how many times in your program
hello()

#name your functions in lowercase, like how you'll name your variables and let it explain what your function does

#you can give your functions parameters, which are pieces of information you give your funciton
#example if you want to give your function a parameter like a name 
#A parameter is a named placeholder for information that a function expects to receive.
#Think of a function as a form: Name - 
#you could do

def sayhi(name) :
    print("Hello " + name)   #Name is a blank space, and we've simply said whenever someone uses this function, expect a name to be given
    
sayhi("Riri") #you have to pass something into the parameter
#This "Riri" becomes an argument, Parameter is the placeholder(name) whiles argument is the actual value (riri)

#you could have many parameters
def more(name, age, fav_color ) :
    print("Hello " + name +  "\nYou are " + age + "\nYour favourite color is " + fav_color)

more("Riri", "21", "blue") #have to make sure they match directly
#remember ints cant be concatenated so you have to put the age in quotation marks to pass as a string or you could do str(age)

"""Default Parameter Values
You can assign default values to parameters. If the function is called without an argument, it uses the default value:

Example
def my_function(name = "friend"):
  print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus")
Example
Default value for country parameter:

def my_function(country = "Norway"):
  print("I am from", country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
"""

#What's the point of functions
#when you need to convert temperature for example from fahrenheit to celsius seceral times in you program
#you need to keep writing the same code for calculation every time
"""temp1 = 77
celsius1 = (temp1 - 32) * 5 / 9
print(celsius1)

temp2 = 95
celsius2 = (temp2 - 32) * 5 / 9
print(celsius2)

temp3 = 50
celsius3 = (temp3 - 32) * 5 / 9
print(celsius3)
"""
#with functions it works like a reusable bottle
"""
def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))
"""
#Functions can send data back to the code that called them using a return statement
#when a function reaches a return statement, it stops executing and sends the result back

#this will return a value
def get_greeting():
  return "Hello from a function"

message = get_greeting()
print(message)

#you can use the returned value directly:
def get_greeting():
  return "Hello from a function"

print(get_greeting())

#f a function doesn't have a return statement, it returns None by default.
"""The pass Statement
Function definitions cannot be empty. If you need to create a function placeholder without any code, use the pass statement:

Example
def my_function():
  pass
The pass statement is often used when developing, allowing you to define the structure first and implement details later."""


#RETURN : functions can return values using the return statement;
#if we want the answer back so that the rest of our program can use it, we use a return 
#There's a difference between print and return
#Print shows something to the user 
#Return says send this value back to the place where the function was called.
def addition(x, y):
  return x + y

result = addition(34, 3)
print(result)

#you can return different data types
#this returns a list 
def stationary():
  return ["pen", "notebook", "eraser", "sharpener"]

needed = stationary()
print(needed[0])
print(needed[1])
print(needed[2])
print(needed[3])

#a function returning a tuple
def display():
  return (10, 20)

x, y = display()
print("x:", x)
print("y:", y)


#you can send arguments with the key = value syntax, also known as keyword arguments (kwargs)
#this way, the order in which you put the parameters/arguments dont matte
def keyword(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

keyword(animal = "dog", name = "Buddy")

def no_order(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

no_order(name = "Buddy", animal = "dog")

#the opposite of that is positional arguments
#When you call a function with arguments without using keywords, they are called positional arguments.
#Positional arguments must be in the correct order, else switching would change the results

def strict_position(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

strict_position("dog", "Buddy")

#it's possible to mix positional and keyword arguments but the positional arguments must come before kwargs
def mixing(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

mixing("dog", name = "Buddy", age = 5)

#again you can specify for a function to have POSITION ONLY arguments using the ",/" after the arguments
def positioning(name, /):
  print("Hello", name)

positioning("Emil")

#To specify that a function can have only keyword arguments, add *, before the arguments:
def just_keywords(*, name):
  print("Hello", name)

just_keywords(name = "Emil")

#Without *,, you are allowed to use positional arguments even if the function expects keyword arguments
#With *,, you will get an error if you try to use positional arguments:
#You can combine both argument types in the same function.
#Arguments before / are positional-only, and arguments after * are keyword-only

#SCOPE
