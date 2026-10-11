"""specify a secret word stored in the program
    user can interact with program to keep guessing what the secret word is
    to be able to type in different words until the get the secret word right
"""

#create a variable with our secret word
secret_word = 'Giraffe'
guesses = ''

#can improve this by setting a limit to what they can guess
count_guesses = 0
#prompting user to get input and keep guessing, would have to use while loop if its not equal to secret word
while guesses != secret_word and count_guesses < 5:
    if count_guesses == 5:
            break
    guesses = input("Enter your guess word: ")
    count_guesses += 1 #after each guess and iteration of loop we can increment guess count
    print(guesses)
if count_guesses == 5:
    print('Nah man, you ran out.')
else:
    print("Girl you smart! You win!")
