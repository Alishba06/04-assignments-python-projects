
import random
from words import words 

def get_valid_word(words):
    word = random.choice(words)
    while '_' in word or ' ' in word:
        word = random.choice(words)
    return word

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    used_letters = set()  

    lives = 6

    print("Welcome to Hangman!")

    while len(word_letters) > 0 and lives > 0:
        print(f"You have {lives} lives left. You have used these letters: {' '.join(used_letters)}")

        word_list = [letter if letter in used_letters else '_' for letter in word]
        print("Current word: ", ' '.join(word_list))

        user_letter = input("Guess a letter: ").lower()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print("Letter is not in word.")
        elif user_letter in used_letters:
            print("You have already used that letter. Try again.")
        else:
            print("Invalid character. Try again.")

    if lives == 0:
        print(f"Sorry, you died. The word was {word}")
    else:
        print(f"Yay! You guessed the word {word}!!")


hangman()
