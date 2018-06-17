# words = ['sunflower', 'tulip', 'daisy']

def wrong_guess_count(word, guesses):
    wrong_guesses = [list(x) for x in guesses if x not in word]
    return len(wrong_guesses)


def is_winner(word, guesses):
    if wrong_guess_count(word, guesses) > 6:
        print ('You Lost!')


def show_guess(word, guesses):
    show = list(word)
    for x in show:
        if x in guesses:
            print (x, end=" ")
        else:
            print ('_', end=" ")


def make_guess(word, guesses):
    is_winner(word, guesses)
    guess = input('Guess a letter ')
    print ('Player wrote: %s' % (guess))
    guesses.append(guess)
    show_guess(word, guesses)

    print ('\n\nNumber of wrong guesses: ' + str(wrong_guess_count(word, guesses)))

    print(show_guess(word, guesses))

    make_guess(word, guesses)


make_guess('sunflower', [])
