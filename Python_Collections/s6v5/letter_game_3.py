import os
import random
import sys

WORDS = [
    'apple',
    'banana',
    'orange',
    'coconut',
    'strawberry',
    'lime',
    'grapefruit',
    'lemon',
    'kumquat',
    'blueberry',
    'melon'
]


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def welcome():
    start = input("Press enter/return to start or Q to quit ").lower()
    if start == 'q':
        print("Bye!")
        sys.exit()
    else:
        return True


def get_guess(guesses):
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1:
            print("You can only guess a single letter!")
        elif guess in guesses:
            print("You've already guessed {}. Try again!".format(guess))
        elif not guess.isalpha():
            print("You can only guess letters!")
        else:
            return guess


def draw(misses, corrects, word):
    clear()
    print('Strikes: {}/7'.format(len(misses)))
    print('\n')

    print("Missed letters:", end=' ')
    for letter in misses:
        print(letter, end=' ')
    print('\n\n')

    for letter in word:
        if letter in corrects:
            print(letter, end=' ')
        else:
            print('_', end=' ')

    print('\n\n')



def play(done):
    clear()
    word = random.choice(WORDS)
    misses = set()
    correct = set()
    word_set = set(word)

    while True:
        draw(misses, correct, word)
        guess = get_guess(misses | correct)

        if guess in word_set:
            correct.add(guess)
            if not word_set.symmetric_difference(correct):
                print("You win!")
                print("The secret word was {}".format(word.upper()))
                done = True
        else:
            misses.add(guess)
            if len(misses) == 7:
                draw(misses, correct, word)
                print("You lost! The secret word was {}".format(word.upper()))
                done = True

        if done:
            if input("Play again? [Y/n]? ").lower() != 'n':
                return play(done=False)
            else:
                sys.exit()

print('Welcome to Letter Guess!')

done = False

while True:
    clear()
    welcome()
    play(done=done)