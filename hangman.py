import string
import random
import os
import sys
import time
import json


def main():

    lives = 8
    guessed = set()

    # Opening words database
    try:
        words = open('words.json')
    except IOError:
        print('Can\'t locate words.json in local directory.')
        time.sleep(3)
        sys.exit()

    with words:
        categories = json.load(words)

    while True:
        print('######################')
        print('---Hangman by Tellu---')
        print('######################\n')

        # Printing all the available categories
        for index, category in enumerate(categories):
            print(f'{index + 1}.{category.title()}')

        # Taking and checking user input
        try:
            choosen_category = int(input(f'\nChoose (1-{len(categories)}): '))
        except ValueError:
            print(f'Only integers!')
        if choosen_category > 0 and choosen_category <= len(categories):
            for index, category in enumerate(categories):
                if (choosen_category - 1) == index:
                    random_word = random.choice(categories[category])
                    break
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        else:
            print(f'There is no category with index {choosen_category}')

        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')

    shown_word = ['_' if letter != ' ' else ' ' for letter in random_word]

    while True:
        print('######################')
        print('---Hangman by Tellu---')
        print('######################\n')

        print(f'Category: {category.title()}')
        print(f'Lives: {lives}\n')

        print(' '.join(shown_word).upper())

        # If he didnt lose and didn't guess all the letters, ask for input
        if lives > 0 and '_' in shown_word:
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
                    lives -= 1
                    print('No!')
                guessed.add(letter)

            # Invalid input handling
            else:
                if len(letter) > 1:
                    print('Slow down there! One letter at a time...')
                    time.sleep(0.5)
                else:
                    print('No special characters!')
        # Endgame
        else:
            # Show the answer if user lost
            if lives < 1:
                print(' '.join(random_word).upper() + ' <- ANSWER')

            # Ask if the user wants to play again
            option = input(
                '\nGame over! Do you want to play again? (Y/N) ').lower()
            if option == 'y' or option == 'yes':
                os.system('cls')
                main()
            elif option == 'n' or option == 'no':
                sys.exit()
            else:
                print('What?')

        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')


def replace_letter(letter, word, hidden_word):
    for index, value in enumerate(word):
        if value == letter:
            hidden_word[index] = letter


main()
