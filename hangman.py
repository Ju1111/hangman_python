# words = ['sunflower', 'tulip', 'daisy']

# def wrong_guess_count(word, guesses):


def show_guess(word, guesses):
    show = list(word)
    for x in show:
        if x in guesses:
            print (x)
        else:
            print ('_')



def make_guess(word, guesses):
    guess = input('Guess a letter ')
    print ('Player wrote: %s' % (guess))
    guesses.append(guess)
    show_guess(word, guesses)


make_guess('sunflower', [])
