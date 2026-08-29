#learning about madlibs game, take any verbs and place it in a story 
#Mad Libs is a word game where one player asks others for a list of words to fill in hidden blanks within a story before reading the funny result aloud
#Got this sample from online. 
#Learned about .capitalize() #Converts the first character to uppercase and remaining characters to lowercase #Works only on strings
#Learned about checking if a string is empty
#Learned how to print a new line "\n", before concatenating with variable
#Learned to put quotations marks in a print statement \"word"\ 
noun = input("Enter a noun:")
adjective = input("Enter an adjective:")
another_adjective = input("Enter another adjective:")
part_of_the_body = input("Enter a part of the body:")
verbs = input("Enter a verb:")
place = input("Enter a name of a place, any place:")
celebrity = input("Enter a celebrity name:")
animal = input("Enter an animal name:")
number = input("Enter a number:")
third_adjective = input("Enter another adjective:")
last_name = input("Enter a last name:")
subject = input("Enter a subject name:")
type_of_food = input("Enter a food: ")
person_in_room = input("Enter a person's name:")
male_name = input("Enter a man name:")
verb_ing = input("Enter a verb that ends with ing:")
exclamation = input("Enter an exclamation:")
another_verb = input("Enter another verb:")

#when i skip one of the variables, it lets me skip with no problems
#can do if else statements, but it'd have to apply to each and check if the string is empty
#can do whiles and then while a variable or string is not empty then print else say which variable is empty 
if (noun == "") : 
    print ("You missed the first noun.")
elif (adjective == "" ) :
    print("You missed the first adjective")
elif (another_adjective =="") :
    print("You missed the second adjective")
elif (part_of_the_body =="") :
    print("Do you not know a part of the body? Missed that fella")
elif (verbs == "") :
    print("You missed the first verb")
elif (place =="") :
    print("You missed the place. Do you not know a place? It literally said any place!")
elif (celebrity =="") :
    print ("C'mon any famous person")
elif (animal == "") :
    print("Just like animals? Maroon 5? A predator? A prey?")
elif (number == "") :
    print ("A number in your phone number")
elif (third_adjective == "") :
    print("Any other adjective, like something that describes a noun")
elif (last_name =="") :
    print ("Maybe your last name?")
elif (subject =="") :
    print ("One you are taught at school, might love or hate.")
elif (type_of_food =="" ) :
    print ("A food, something you eat? You missed that.")
elif (person_in_room =="") :
    print ("They don't have to be there with you now. Just a person in general. We gotta do it.")
elif (male_name =="") :
    print("Quite hard to think of a man's name, but we can't leave it empty, gotta go back.")
elif (verb_ing == "") :
    print ("Just something you're \"doing\". Have to do it")
elif (exclamation == "") :
    print("You missed putting anything in this")
elif (another_verb == "") :
    print("Well you filled in everything else and missed this, have to put something in.")
else : 
    print("Convincing your " + noun + " to let you stay up past your bedtime to play video games can be " + adjective + ", but its not impossible. \n Here are some "+ another_adjective + " excuses to use when you need one last game before bed time. \n  My " + part_of_the_body + " hurts. The only way it'll feel better is if I " + verbs + " these cyborgs and save the " + place + ". "
+ celebrity.capitalize() + " also plays "+ animal + " Hut so if you want me to be successful in life, please give me " + number + " minutes to finish the " + third_adjective + " level. \n Mrs. " +  last_name.capitalize() + ", my " + subject + " teacher, said that video games make you smart."
"She plays " + type_of_food + " Assault, so she knows. \n There's nothing else to do. " + person_in_room.capitalize() + " isn't here to play with, Grandpa " + male_name.capitalize() + " went to bed, and its " + verb_ing + " outside." + "\n", exclamation.capitalize() + "! If you let me play Night " + another_verb + ", I'll clean my room. Think about it pweees :)" )
