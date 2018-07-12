import random

words = ['amsterdam', 'london', 'berlin', 'copenhagen', 'oslo', 'paris', 'brussels', 'dublin', 'belfast', 'stockholm',
         'helsinki', 'vienna','sofia', 'sarajevo', 'prague', 'zagreb', 'athens', 'budapest', 'rome', 'warsaw', 'lisbon',
         'bucharest', 'bratislava', 'madrid', 'bern']


def wrong_guess_count(word, guesses):
    wrong_guesses = [list(x) for x in guesses if x not in word]
    return len(wrong_guesses)


def winner(word, guesses):
    if word == show_guess(word, guesses):
        print ('Yaaaaay, you won!')
        print ('The city was indeed ' + word.upper())
        return play_again()
    elif wrong_guess_count(word, guesses) > 6:
        print ('You Lost!')
        print ('The correct city would have been ' + word.upper())
        return play_again()
    else:
        return True


def play_again():
    question = input('\nDo you want to play again (y/n)? ')
    if question.lower() == 'y':
        make_guess(random.choice(words), [])
    elif question.lower() == 'n':
        return False
    else:
        print ('Please chose y or n')
        play_again()


def show_guess(word, guesses):
    show = list(word)
    result = ''
    for x in show:
        if x in guesses:
            result += x
        else:
            result += '_'
    return result


def print_word(result):
    print(" ".join(result))


def skip_duplicate(guess, guesses):
    if guess in guesses:
        print('You have already guessed ' + guess.upper())
        print('Please choose a different letter')
        return True


def make_guess(word, guesses):
    if not winner(word, guesses):
        return

    if len(guesses) == 0:
        print("Welcome to the european capitals hangman. Please choose a letter to guess the first city.")

    guess = input('Guess a letter ').lower()

    if skip_duplicate(guess, guesses):
        make_guess(word, guesses)
    else:
        print ('Player wrote: %s' % (guess))
        guesses.append(guess)
        print_word(show_guess(word, guesses))

        print ('\n\nNumber of wrong guesses: ' + str(wrong_guess_count(word, guesses))+'\n')

        if wrong_guess_count(word, guesses) <= 7:
            make_guess(word, guesses)


make_guess(random.choice(words), [])
