# words = ['sunflower', 'tulip', 'daisy']

def wrong_guess_count(word, guesses):
    wrong_guesses = [list(x) for x in guesses if x not in word]
    return len(wrong_guesses)


def show_guess(word, guesses):
    show = list(word)
    for x in show:
        if x in guesses:
            print (x, end=" ")
        else:
            print ('_', end=" ")


def make_guess(word, guesses):
    guess = input('Guess a letter ')
    print ('Player wrote: %s' % (guess))
    guesses.append(guess)
    show_guess(word, guesses)
    wrong_guess_count(word, guesses)


make_guess('sunflower', [])
