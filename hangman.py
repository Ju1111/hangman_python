words = ['sunflower', 'tulip', 'daisy']

# def wrong_guess_count(word, guesses):

def make_guess(word, guesses):
    guess = input('Guess a letter ')
    print ('Player wrote: %s' % (guess))
    guesses.append(guess)
    print(guesses)

make_guess('sunflower', [])
