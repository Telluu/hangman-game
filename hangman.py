import string
import random
import time
import os
import sys


def main():

    words = ['hello world']
    guessed = []
    lifes = 8

    random_word = random.choice(words)
    shown_word = ['_' if letter != ' ' else ' ' for letter in random_word]

    while True:
        print('######################')
        print('---Hangman by Tellu---')
        print('######################\n')

        print(f'Lifes: {lifes}\n')

        print(' '.join(shown_word).upper())

        # If he didnt lose and didn't guess all the letters, ask for input
        if lifes > 0 and '_' in shown_word:
            letter = input('\nGuess: ').lower()

            # If input is a letter
            if len(letter) == 1 and letter in string.ascii_letters:
                # And not already tried letter
                if letter in guessed:
                    print('You guessed it earlier!')
                # And is in a random word
                elif letter in random_word:
                    # Then replace a letter using a func
                    replace_letter(letter, random_word, shown_word)
                    print('Yes!')
                else:
                    # Else subtract one life
                    lifes -= 1
                    print('No!')
                guessed.append(letter)

            # Invalid input handling
            else:
                if len(letter) > 1:
                    print('Slow down there! One letter at a time...')
                    time.sleep(0.5)
                else:
                    print('No special characters!')
        # Endgame
        else:
            if lifes < 1:
                print(' '.join(random_word).upper() + ' <- ANSWER')
            option = input(
                '\nGame over! Do you want to continue? (Y/N) ').lower()
            if option == 'y' or option == 'yes':
                os.system('cls')
                main()
            elif option == 'n' or option == 'no':
                sys.exit()
            else:
                print('What?')

        time.sleep(1)
        os.system('cls')


def replace_letter(letter, word, hidden_word):
    for index, value in enumerate(word):
        if value == letter:
            hidden_word[index] = letter


main()
