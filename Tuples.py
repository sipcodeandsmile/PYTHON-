##Tuples are data structures, a container where you can store different data types
#Similar to lists, bit has a key few differences
#Tuple is a collection which is ordered and unchangeable

#To create a tuple, you have to write it with round brackets
firsttuple = ("apple", "banana", "pawpaw")
print(firsttuple)

#but you can also represent it without parentheses:
thistupe = "apple", "berry", "blackberry"
print(thistupe)
print(thistupe(1))

#Tuple are indexed, the same way a list is indexed, starting from 0
#Tuples are ordered, that means items must have a defined order, and that order will not change compared to a list
#Tuple are also unchangeable, meaning that items cannot change, add or remove items after a tuple has been created
#because tuples are indexed, it can have items with the same value 

#example
duplicatetuple = ("Benjamin", "Beyonce", "Berncie", "Benjamin")
print(duplicatetuple)

#we can determine how many items a tuple had using the len() function
duplicatetuple = ("Benjamin", "Beyonce", "Berncie", "Benjamin")
print(len(duplicatetuple))

#if you want a tuple with just only one items, you have to add a comma after the item else python won't recognize it as a tuple
onetuple = ("bag",)
print(type(onetuple))

#not a tuple
nottuple = ("pen")
print(type(nottuple))

#to create an empty tuple, you don't need anyhting in it, just your brackets
#to create an empty tuple, you don't need anyhting in it, just your brackets
emptytuple = ()
print(type(emptytuple))

#tuples can be of any data type but also can contain different data types
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
tuple4 = ("Ian", 75, False, 37, "me")


#From Python's perspective, tuples are defined as objects with the data type 'tuple':
#<class 'tuple'>
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

#the tuple() constructor could also be used to make a tuple
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

#you need to be aware of the collection type you're choosing as 
#you can store data that never needs to be changed/remains the same for a tuple for efficiency

