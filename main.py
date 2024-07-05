import string
import random
from words import words

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)

    alphabet = set(string.ascii_uppercase)
    word_letters = set(word)
    used_letters = set()
    
    lives =  6
    
    while len(word_letters) > 0 and lives > 0:
        print('You have ', lives, 'lives left and you have used these letters: ',' '.join(used_letters))
        letter_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ',' '.join(letter_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
             used_letters.add(user_letter)
             if user_letter in word_letters:
                 word_letters.remove(user_letter)

             else:
                 lives = lives - 1
                 print("This letter isn't in the word.")

        elif user_letter in used_letters:
             print("You've entered this letter.")

        else:
             print("Invalid character. Please try again.")
    
    if lives == 0:
         print('The man is hung, sorry. The word was', word,'.')
    
    else:
        print('You guess the word! It is ', word, '!')

hangman()