#Learning if else statements. you have if elif(elseif) and else, the semicolon tells the console there is a block of code that happens in here, then indentation allows for that code to stay in
#you must order your elif chain from most specific/strict to least strict, so the narrowest, most exclusive condition gets first chance to catch it.
#python runs from top to bottom

score = 75
if score >= 90:
    print ("A")
elif score >= 80:
    print("B") 
elif score >=70:
    print("C")
else: 
    print("F") 


is_hungry = True
is_cooking = False
buy_food = True

if is_hungry and is_cooking:
    print("What are we gonna get")

else: 
    print("I think we have some pasta, we can make that")


#trying to use functions and return
def max_num(num1, num2, num3) :
    if num1 >= num2 and num1 >= num3 :
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else: 
        return num3
    
print(max_num(95, 43, 123))

#we can compare strings, essnentially asking if this is that
def compare(name, false) :
    if "Farida" == "Riri" :
        return name
    else: 
        return false

#Short Hand If ... Else
#If you have one statement for if and one for else, you can put them on the same line using a conditional expression:
a = 2
b = 330
print("A") if a > b else print("B")

#you can assign a value like how you'd do a variable with if else
elisha = 23
bygan = 43
bigger = elisha if elisha > bygan else bygan
print("Bigger is " + str(bigger))

#and - Returns True if both statements are true
#or - Returns True if one of the statements is true
#not - Reverses the result, returns False if the result is true

#You can have if statements inside if statements. This is called nested if statements.
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
    
#rhe inner if statement only runs if the outer condition (x > 10)
#Each level of nesting creates a deeper level of decision-making. The code evaluates from the outermost condition inward.
#a nested if can be simplified by simply using logic operators


"""Why Use pass?
The pass statement is a null operation, so nothing happens when it executes, no error is produced because an if statement can't be empty, this allows it to be empty

When you're creating code structure but haven't implemented the logic yet
When a statement is required syntactically but no action is needed
As a placeholder for future code during development
In empty functions or classes that you plan to implement later
pass in Development
During development, you might want to sketch out your program structure before implementing the details. The pass statement allows you to do this without syntax errors."""

#using pass with multople conditions
value = 50

if value < 0:
  print("Negative value")
elif value == 0:
  pass # Zero case - no action needed
else:
  print("Positive value")
  

#using pass with functions
def calculate_discount(price):
  pass # TODO: Implement discount logic

# Function exists but doesn't do anything yet


age = 20

if age > 13 :
    print("Child")
elif age > 18 :
    print("Teenager")
else :
    print("Adult")
