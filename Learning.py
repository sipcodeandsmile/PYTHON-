from math import *
print("Hello World")
"""
print("Below is a right-angle triangle")
print("   /|")
print("  / |")
print(" /  |")
print("/___|")
"""

"""""
print("Below is a square")
print("________")
print("|      |")
print("|      |")
print("|______|")
"""

#Variables and data types
#Program could have various data and values to manage, so a variable allows us to store data values in a sort of container
print("There was a girl named Farida, ")
print("she was learning how to code in python at 25 years old.")
print("She really enjoyed learning python")
print("but didn't like her laptop's functionality.")
#But we want to change the character's name or age, we would have to manually change it everywhere its mentioned
#A variable allows us to change once, since we can store the characters name and age or anything else and let the changes apply automatically
#have to assign the name to the container/variable
character_name = "Ella"
character_age = "50"
print("There was a girl named " + character_name + ", ") #The + is basically saying i want to join this info with this info with this info and without it before and after the variable's name, they'd be an error
print("she was learning how to code in python at " + character_age + " years old.")

#IF you want to all of a sudden change the variable, you can assign a new value to it 
character_name = "Sunny"
character_age = 50 #you don't really store numbers in quotation marks if you want
is_Female = True #this data type is a boolean value which allows you to store true or false values 
print(character_name + " really enjoyed learning python")
print("but didn't like her laptop's functionality.")


#STRINGS
#Need quotation marks and put a string/text inside of it
print("1") #this prints the number 1 but as a string
print("Learning about strings now") 
print("Learning about strings now \n creates a new line") # this separates everytext before it on one line and the text after the \n on another line
print("Learning about strings now \ this for  python to print a quotation mark without errors") #This for backslash
#making string variable
name = "Farida" #made a string variable called name and print that out
print(name)
#CONCATENATION - taking/joining strings together
print(name + " is learning python!")
#FUNCTIONS - block of code that can be run and performs a specific tasks/operation when called
#can use it to modify our strings but also get information about our strings
print(name.lower()) #this takes the entire text adn changes it to lower, pay mind to the syntax
print(name.upper()) #this takes the entire text changes it to upper, pay mind to the syntax
print(name.isupper()) #checks if a phrase is in all caps or lower caps, would return a true/false statement. Should return false because name is not all caps. i'm asking, through boolean text is in uppercase
print(name.upper().isupper()) #combining functions. converts to upper first and then checks if upper its upper
print(len(name)) #giving the length function the phrase to tell me how many characters are in it
print(name[3]) #can print individual characters. if we want i of string, thats the fourth character. when working with string, count/index starts from 0
print(name[0]) #would print F. because its first character
#.index() tells us where a specific character is located. you can give this a value which is referred to as passing a parameter
phrase = "Riri nibbles"
print(phrase[0]) #prints R
print(phrase.index("R")) #should print 0 which is where R is
print(phrase.index("i"))
print(phrase.index(" nib")) #can put here and it would show where it starts which is 4
#print(phrase.index("F")) #would throw an error because is not in there
#this can be used for replacing 
print(phrase.replace("nibbles", "Eats")) #this allows you to replace certain words or letters inside strings with new ones, you take the old phrase and put the new phrase after a comma after it



#NUMBERS
#Can normally print numbers and do arithmetic operations like this. Only have numbers when you want to do mathematical operations, else leave it as strings
print(2)
print(-4.553)
print(3/4) #this would print out 0.75
print (2*7)
#for more complex operations we can specify the order of operations like this
print(2*3-4) #This would print 2 because python takes it from a sort of left to right reading and doesn't follow the idea of bodmas unless
print(2 * (3-4)) #This would perform the operation in the brackets first, giving -1 and then multiply 2* that repsonse. 
#Brackets help with the order of things
print(11 % 3) #this takes the first number, divides it by the second number and produces the remainder from the division so 11 divided by 3 gives 3 remainder 2 what becomes the remainder?
#we can store our numbers in variables
first_num = 4
print (first_num)
#guess what you can change a number to a string 
print (str(first_num))  #it would print out 4 but not as a number, as a string
#comes in handy if you want to print numbers with strings because using a number data type (int) and string output produces an error
print (str(first_num) + " and 5 go together")

#MATH FUNCTIONS - function is a collection of code doing something 
num = -4
print(abs(num)) #abs is for absolute values
print(pow(3, 8)) #with pow, you can give it 2 pieces of info. 1st could be a number and second the power you want to take that to. so this is 3 to the power of 8
print(pow(num, 2))
print(max(num, 2)) #max returns which of the two numbers is bigger
print(min(num, 2)) #does the opposite of max
print(round(3.6)) #rounding numbers

#There are more further advanced math operations but we'd have to import (see top of document)
print(floor(3.4)) #takes the lowest number and chops off everything
print(floor(3.471)) #takes the lowest number and chops off everything after decimal point, rounds up
print(ceil(3.4)) #takes and rounds up
print(sqrt(144))
print(cbrt(27))


#GETTING INPUT FROM USER
#input("What is your favorite color?") this lets python know we want to get input from user and allows a user to type in something and takes it. 
#the prompt which goes on our end in the brackets lets the user know what kind of information to put
#we can store whatever the user puts into a program inside a variable. So to make a program that gets a users fav color and prints oh nice
color = input("What is your favorite color?") #now the value that the user gives would be stores in the variable color
song = input("Favorite song: ")
print("Wow " + color + " is a nice color:)\nI have never heard of " + song + " before:(")






#Learning if else statements. you have if elif(elseif) and else, the semicolon tells the console there is a block of code that happens in here, then indentation allows for that code to stay in
#you must order your elif chain from most specific/strict to least strict, so the narrowest, most exclusive condition gets first chance to catch it.
#python runs from top to bottom
"""_summary_
score = 75
if score >= 90:
    print ("A")
elif score >= 80:
    print("B") 
elif score >=70:
    print("C")
else: 
    print("F") 
"""
