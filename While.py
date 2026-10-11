#Allows to execute a block of code multiple times/while something is true and stops immediately a condition is false
#syntax: while condition :
#           print
#           have an increment

# print i as long as i is less than 6
i = 1
while i < 6:
    print(i)
    i += 1 #increments i by 1

print("Done with loop")
#we can have a break statement that allows us to break the loop even when the condition is still true
i = 9
while i < 15:
    print(i)
    if i == 12:
        break
i += 1
print("Broke it")

#When and why would we need a break in our program, especially a large program
