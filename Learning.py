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
