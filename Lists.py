#Because you will be dealing with a lot of different data in a python program
#A list can help you manage and organise it properly. 
#Lists essentially helps you store lists of information in python. So you can put a bunch of different data values in a list and work with them, basically organising them helps making them easy to handle

#basics of using lists
#give it a descriptive name, and use the open/closed square brackets to put your values in
Fruits = ["Pear", "Pawpaw", "Pineapple","Apple", "Cocoa", "Strawberry"] #with lists you can store multiple values and access them. 
#You can have anything in your lists ex: subjects =["John", 3, True]
print(Fruits) #prints everything in the list
#to access individual elements you have to use their index which starts from 0
print(Fruits[1]) #prints out pawpaw because its index is 1
print(Fruits[-1]) #prints the last thing in the list, because we're going from the back of the list/right to left
print(Fruits[1:]) #prints pawpaw, pineapple  and everything after pawpaw because it grabs what's ar index positon 1, and  everything after it
print (Fruits[1:3]) #grabs all the elements from index ppsotion one up to psotion 3 but doesnt include position 3, will only print pawpaw and pineapple
Fruits[1] = "Blueberry" #this modifies/changes the lists, so now index one is blueberry not pawpaw 
#original_list = ['apple', 'banana', 'cherry']
#capitalized_list = []
#using a for loop
#for word in original_list:
    #capitalized_list.append(word.capitalize())
#print(capitalized_list)
# output = ['Apple', 'Banana', 'Cherry']
#using comprehension
#original_list = ['apple', 'banana', 'cherry']
#capitalized_list = [word.capitalize() for word in original_list]
#print(capitalized_list)
#using map - map is a function that allows a function to be applied to all items  in a list, the str.captialize function is what capitalizes each string in the list
#original_list = ['apple', 'banana', 'cherry']
#capitalized_list = list(map(str.capitalize, original_list))
#print(capitalized_list)
#using join- useful when you want to create a single, space-separated string rather than a list.
#original_list = ['apple', 'banana', 'cherry']
#capitalized_string = ' '.join(word.capitalize() for word in original_list)
#print(capitalized_string)
#using lambda with map finction 
#strings = ["hello", "world", "python"]
#capitalized_strings = list(map(lambda x: x.capitalize(), strings))
#print(capitalized_strings)

#USING FUNCTIONS WITH LISTS
even_number = [2, 4, 8, 10, 22, 16, 14, 2, 36]
awards = ["Golden Globe", "Oscar", "Baftas", "Grammy's", "Emmy"]
#this extend function below allows you to take a list, and add another list to the end of it 
#awards.extend(even_number) 
#print(awards) #this would print out everything in awards list and add the everything in even_numbers list after Emmy, at the end
#awards.append("MTV") = allows you to add an element to the end of the list
#awards.insert(1, "MTV") - allows you to insert to a specific place, so put in the position 1st and then put in the value
#print(awards) - would look like ["Golden Globe", 'MTV', "Oscar", "Baftas", "Grammy's", "Emmy"] comapred to the append where it would just be at the end
#awards.remove("Oscar") - removes oscar from the list
#awards.clear() - removes everything from the list
#awards.pop() - removes/pops off the last element off the list
#Looking for certain elements in the list
print(even_number.index(2)) #returns the index positon of 2
#list.index(element, start, end) - element is the item you're looking for, start(optional) where the search begins, end(optional) where it stops
print(even_number.index(16, 2)) #or print(even_number.index(16, 2,6))
#it will always return the positon of the first occurrrence of the vallue, even if there are duplicates
#with tuple elements 
a = [("Emma", 21), ("Lucas", 22), ("Sophia", 20)]
res = a.index(("Lucas", 22))
print(res)
#a.index(("Lucas", 22)) searches for the exact tuple ("Lucas", 22) and tuple is found at index 1
print(even_number.count(2))  #prints out how many times 2 is in the list
#even_number.sort() #will sort the list, auotmaticall ascending order
awards.sort() #in ascending order
print(even_number)
print(awards)
even_number.reverse() #prints it out in reverse orders, from the end of the list to the begininh
print(even_number)

#copying a list
awards_copy = awards.copy()
print(awards_copy)


#QUESTION: But what if you have a long lists, how do you find the index?

#TUPLES
