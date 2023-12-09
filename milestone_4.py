import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = self._get_random_word()
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters_left = len(set(self.word))
        self.list_of_guesses = []

    def _get_random_word(self):
        return random.choice(self.word_list)
    
    def check_guess(self, single_letter_guess):
        if single_letter_guess in self.word:
            print(f"Great! {single_letter_guess} is in the word.")
            for index, letter in enumerate(self.word):
                if single_letter_guess == letter:
                    self.word_guessed[index] = letter           
            self.num_letters_left -= 1        
            print("You have {num_lives} lives left.")

        else:           
            self.num_letters_left -= 1 
            print(f"Sorry, {single_letter_guess} is not in the word. Try again.")  
            print("You have {num_lives} lives left.")
    
    def ask_for_input(self):
        while True:
            single_letter_guess = input("Enter a single letter: ")
            
            if not(single_letter_guess.isalpha() and len(single_letter_guess) == 1):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif single_letter_guess in self.list_of_guesses:
                print("Oops!You already tried that letter!")                    
            else: 
                self.check_guess(single_letter_guess)
                self.list_of_guesses.append(single_letter_guess.lower())
                
list_of_favourite_fruit = [
    "apple",
    "banana",
    "orange",
    "pear",
    "tomato"
]                
                
person1 = Hangman(list_of_favourite_fruit)              
person1.ask_for_input()    