# words = ['sunflower', 'tulip', 'daisy']

def wrong_guess_count(word, guesses):
    wrong_guesses = [list(x) for x in guesses if x not in word]
    return len(wrong_guesses)


def is_winner(word, guesses):
    if word == show_guess(word, guesses):
        print ('Yaaaaay, you won!')
        play_again()
    if wrong_guess_count(word, guesses) > 6:
        print ('You Lost!')
        play_again()


def play_again():
    question = input('Do you want to play again (y/n)? ')
    if question.lower() == 'y':
        make_guess('tulip', [])
    else:
        return False


def show_guess(word, guesses):
    show = list(word)
    result = ''
    for x in show:
        if x in guesses:
            result += x
        else:
           result += '_'
    return result


def make_guess(word, guesses):
    guess = input('Guess a letter ')
    print ('Player wrote: %s' % (guess))
    guesses.append(guess)
    print (show_guess(word, guesses))

    print ('\n\nNumber of wrong guesses: ' + str(wrong_guess_count(word, guesses))+'\n')

    if wrong_guess_count(word, guesses) < 7:
        make_guess(word, guesses)
    else:
        is_winner(word, guesses)


make_guess('sunflower', [])
