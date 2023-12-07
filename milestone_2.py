import random

list_of_favourite_fruit = [
    "apple",
    "banana",
    "orange",
    "pear",
    "tomato"
]

print(list_of_favourite_fruit)

word = random.choice(list_of_favourite_fruit)

print("Randomly chosen word:", word)


single_letter_guess = input("Enter a single letter: ")

if single_letter_guess.isalpha() and len(single_letter_guess) == 1: # checking if the input is alphabetical and of single length
    print("Good guess!")
    
else:
    print("Oops! That is not a valid input.")    
    