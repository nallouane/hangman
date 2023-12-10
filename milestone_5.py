import random

class Hangman:
    def __init__(self, word_list, num_lives_left=5):
        self.word_list = word_list
        self.num_lives_left = num_lives_left
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

        else:           
            self.num_lives_left -= 1 
            print(f"Sorry, {single_letter_guess} is not in the word. Try again.") 
        
        print(self.word_guessed)
        print(f"You have {self.num_lives_left} {'lives' if self.num_lives_left == 1 else 'life'} left.")    
        print(f"You have {self.num_letters_left} {'letters' if self.num_letters_left == 1 else 'letter'} left.")
    
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
                break
                
def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)                
    while True:
        if game.num_lives_left == 0:
            print("You lost!")
            break
        elif game.num_letters_left == 0:
            print("Congratulations. You won the game!")
            break
        else:
            game.ask_for_input()
                    

list_of_favourite_fruit = [
    "apple",
    "banana",
    "orange",
    "pear",
    "tomato"
]                
                    
play_game(list_of_favourite_fruit)                           