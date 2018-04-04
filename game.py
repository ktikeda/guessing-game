"""A number-guessing game."""

import random

def guessing_game():

    user_name = raw_input("Hi! What's your name?:")

    playing = True
    all_scores = []

    while playing:

        random_num = random.randint(1,100)

        print("{}, I'm thinking of a number between 1 and 100.".format(user_name))
        print('Try to guess my number.')

        total_tries = 0
        guess = raw_input('Your guess?:')
        validation_results = val_guess(guess, total_tries)

        guess = validation_results[0]
        total_tries = validation_results[1]

        while guess != random_num:
            if guess > random_num:
                guess = raw_input("Your guess is too high, try again.\nYour guess?:")
            elif guess < random_num:
                guess = raw_input("Your guess is too low, try again.\nYour guess?:")
            validation_results = val_guess(guess, total_tries)
            guess = validation_results[0]
            total_tries = validation_results[1]

        print "Well done, {}! You found my number in {} tries!\n".format(user_name, total_tries)

        if len(all_scores) > 1:
            if total_tries < best_score:
                print "Congratulations! {} tries is your best score!\n".format(total_tries)
            elif total_tries == best_score:
                print "You've matched your best score of {} tries!\n".format(total_tries)
            else:
                print "Your best score so far is {} tries!\n".format(best_score)
        
        all_scores.append(total_tries)
        best_score = min(all_scores)

        play_again = raw_input("Would you like to play again? Enter 'Y' for 'yes' or 'N' for 'no.':")
        play_again = play_again.lower()
        while play_again != 'n' and play_again != 'y':
            play_again = raw_input("Sorry, I didn't get that. Would you like to play again? Enter 'Y' for 'yes' or 'N' for 'no.':")
        if play_again == 'y':
            continue
        elif play_again == 'n':
            playing = False

def val_guess(user_input, c_tries):
    while True:
        try:
            user_input = int(user_input)
        except ValueError:
            user_input = raw_input("Sorry, your guess is not a valid number. Please choose a number between 1 and 100.:")
            c_tries += 1
            continue
        if user_input < 1 or user_input > 100:
            user_input = raw_input("Sorry, your guess is out of range. Please choose a number between 1 and 100.:")
            c_tries += 1
            continue
        else:
            break
    c_tries += 1
    return (user_input, c_tries)


guessing_game()

