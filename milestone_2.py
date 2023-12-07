import random

word_list = [
    "apple",
    "banana",
    "orange",
    "pear",
    "tomato"
]

print(word_list)

word = random.choice(word_list)

print("Randomly chosen word:", word)


guess = input("Enter a single letter: ")

if guess.isalpha() and len(guess) == 1:
    print("Good guess!")
    
else:
    print("Oops! That is not a valid input.")    
    