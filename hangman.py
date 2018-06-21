import random

words = ['sunflower', 'tulip', 'daisy', 'lilly']


def wrong_guess_count(word, guesses):
    wrong_guesses = [list(x) for x in guesses if x not in word]
    return len(wrong_guesses)


def winner(word, guesses):
    if word == show_guess(word, guesses):
        print ('Yaaaaay, you won!')
        return play_again()
    elif wrong_guess_count(word, guesses) > 6:
        print ('You Lost!')
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


def make_guess(word, guesses):
    if not winner(word, guesses):
        return

    guess = input('Guess a letter ')
    print ('Player wrote: %s' % (guess))
    guesses.append(guess)
    print (show_guess(word, guesses))

    print ('\n\nNumber of wrong guesses: ' + str(wrong_guess_count(word, guesses))+'\n')

    if wrong_guess_count(word, guesses) <= 7:
        make_guess(word, guesses)


make_guess(random.choice(words), [])
