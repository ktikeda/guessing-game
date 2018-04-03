"""A number-guessing game."""

def guessing_game():
    user_name = raw_input("Hi! What's your name?:")
    import random
    random_num = random.randint(1,100)

    print("{}, I'm thinking of a number between 1 and 100.".format(user_name))
    print('Try to guess my number.')

    guess = raw_input('Your guess?:')
    guess = val_guess(guess)
    tries = 1

    while guess != random_num:
        if guess > random_num:
            guess = raw_input("Your guess is too high, try again.\nYour guess?:")
            guess = val_guess(guess)
            tries += 1
        elif guess < random_num:
            guess = raw_input("Your guess is too low, try again.\nYour guess?:")
            guess = val_guess(guess)
            tries += 1

    print "Well done, {}! You found my number in {} tries!".format(user_name, tries)

def val_guess(user_input):
    while True:
        try:
            int(user_input)
        except:
            user_input = raw_input("Sorry, that is not a valid guess. Please choose a number between 1 and 100.:")
            continue
        if int(user_input) < 1 or int(user_input) > 100:
            user_input = raw_input("Sorry, that is not a valid guess. Please choose a number between 1 and 100.:")
            continue
        else:
            break
    return int(user_input)


guessing_game()

