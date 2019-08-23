import string
import random
import time
import os


def main():

    words = ['hard hangman']
    guessed = []
    lives = 8

    random_word = random.choice(words)
    shown_word = ['_' if letter != ' ' else ' ' for letter in random_word]

    while True:
        print('######################')
        print('---Hangman by Tellu---')
        print('######################\n')

        print(f'Lives: {lives}\n')

        print(' '.join(shown_word).upper())
        if lives < 1:
            print(' '.join(random_word).upper() + ' <- ANSWER')
        print('')

        if lives > 0 and '_' in shown_word:

            letter = input('Guess: ').lower()

            if len(letter) == 1 and letter in string.ascii_letters:
                if letter in guessed:
                    print('You guessed it earlier!')
                elif letter in random_word:
                    replace_letter(letter, random_word, shown_word)
                    print('Yes!')
                else:
                    lives -= 1
                    print('No!')
                guessed.append(letter)
            else:
                if len(letter) > 1:
                    print('Slow down there! One letter at a time...')
                    time.sleep(1)
                else:
                    print('No special characters!')
        else:
            option = input(
                'Game over! Do you want to continue? (Y/N) ').lower()
            if option == 'y':
                os.system('cls')
                main()
            elif option == 'n':
                return
            else:
                print('What?')

        time.sleep(1)
        os.system('cls')


def replace_letter(letter, word, hidden_word):
    for index, value in enumerate(word):
        if value == letter:
            hidden_word[index] = letter


main()
