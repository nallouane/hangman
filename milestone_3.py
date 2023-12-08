import random
    
list_of_favourite_fruit = [
    "apple",
    "banana",
    "orange",
    "pear",
    "tomato"
]

print(list_of_favourite_fruit)

random_word_from_list_of_favourite_fruit = random.choice(list_of_favourite_fruit)

def ask_for_input():
    while True:
        single_letter_guess = input("Enter a single letter: ")
        
        if single_letter_guess.isalpha() and len(single_letter_guess) == 1:
            print("Good guess!")
            return single_letter_guess.lower()
        else:
            print("Oops! That is not a valid input. Please enter a single letter.")

def check_guess(single_letter_guess, word):
    if single_letter_guess in word:
        print(f"Great! {single_letter_guess} is in the word.")

    else:
        print(f"Sorry, {single_letter_guess} is not in the word. Try again.")    
                            
check_guess(ask_for_input(), random_word_from_list_of_favourite_fruit)