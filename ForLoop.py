"""Allows us to loop for iterating over different collections like lists, dictionaries, 
    tuples, set or a letters in a  string.
    We can use this to execute a set of statements, once for each item in a list or set ir whatever
"""
#the variable would represent a different value each time we go through the loop
for letter in "Giraffe Academy": #this is basically saying for every letter in this string, I want to do something
    print(letter) #this is going to print out each and every character in the string, even the space

#using a list
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

#again we cab use a break statement(and merge that with if statements)
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

#this actually ends up printing both apple and banana
#in this case the break comes before the print 
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)
print('We got ' + x)   
#so it would go through the list, apple doesn't equal banana so it would print x, 
#but then the next x is banana, so it breaks before proceeding 
#if we print(x) outside of it we get our banana again

#we can still have an else in a for loop
#this specifies a block of code to execute when the loop is finished
for x in range(6):
    print(x)
else:
    print("Finally finished!")
#intro to range
for number in range(10):
    print(number)
#this would print every number staring from 0 till 10 but not including 10
for num in range(3,10) : #start from 3 stop at 10
    print(num) #again everything to 10

#interestingly we can use that to loop through our lists 
list_of_games = ['Mahjong', 'Sudoku', 'Monopoly', 'Oware', 'GTA', 'Ampe', 'Chess', 'Ludo']
for name in range(len(list_of_games)): #can pass the length of the list as our range, so it should tell python range of 8
    #again it won't print 8 but start from 0-7 and that is technically the true index of the list since its index starts from 0
    print(list_of_games[name]) #able to access each individual game/name of game
    
#the range function defaults to increment by one but we can specifify by how much we want to increment by adding a third parameter
for x in range(0, 20, 2): #ends op printing the even numbers between 0 and 20, but its just gonna go from 0 and increase by 2 so then 2 then increase by 2 so 4
    print(x) #you must have your range(start, stop, step)

list_of_games = ['Mahjong', 'Sudoku', 'Monopoly', 'Oware', 'GTA', 'Ampe', 'Chess', 'Ludo']
for name in range(0, len(list_of_games), 2): #can pass the length of the list as our range, so it should tell python range of 8
    #again it won't print 8 but start from 0-7 and that is technically the true index of the list since its index starts from 0
    print(list_of_games[name]) #able to access each individual game/name of game

print(list_of_games[name])

#there's a slicing method for lists that allows you to start/stop wherever 
for name in list_of_games[::2]:
    print(name)  #this allows you to start from the very beginning of the list's index 0 all the way to the end and steps/increments by 2

list_of_games[2:6] #lets us start at index 2 and end at 6 but not including 6
list_of_games[:4] #automatically start from the beginning, index 0 and ends before index 4/doesn't include index 4
list_of_games[4:] #other way round, from index for the the end, including the last index
list_of_games[::-1] #negative steps allows us to count/start from the back. so instead of begining to end,i it's end to beginning


#making a function for exponents using for loop
def raise_to_the_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result
print(raise_to_the_power(2,3)) #our base number is 2 and power number is 3
#expecting the for loop to run three times even though it will take 0,1,2
"""* **Initial State:** `result = 1`
* **Iteration 1 (index = 0):** `result = 1 * 2` (result is now `2`)
* **Iteration 2 (index = 1):** `result = 2 * 2` (result is now `4`)
* **Iteration 3 (index = 2):** `result = 4 * 2` (result is now `8`)
* **End:** Loop finishes because it ran 3 times, and it returns `8`.

"""
#It behaves this way because `range()` always generates a sequence of integers starting from `0` up to (but not including) the number you pass in, so the 3
