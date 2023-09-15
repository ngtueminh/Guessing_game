"""guess_game_fun
Guess Game with a Function
In this project the guess game is recast using a function
"""
import random

prompt = "What is your guess?"

# New constants
quit = -1
quit_text = 'q'
quit_message = "Thanks you for playing"
comfirm_quit_message = "Are you sure want to quit (Y/n)? "

#New cofirm_quit_function
def confirm_quit():
    """Ask player to confirm that they want to quit
    default to yes
    Return True (yes, quit) or False (no, don't quit)"""
    spam = input(comfirm_quit_message)
    if spam == 'n':
        return False
    else:
        return True

def do_guess_round():
    """Choose a random number, ask for players for a guess
    check whether the guess is true
    and repeat until the player is correct"""
    computer_number = random.randint(1,100) 
    number_of_guesses = 0 #Added
    while True:
        player_guess = input(prompt)
        #New if clause to test against quit
        if player_guess == 'q':
            if confirm_quit():
                return quit
            else:
                continue #this is, do next round of loop
        number_of_guesses = number_of_guesses + 1 #Added 
        if computer_number == int(player_guess):
            print("Correct!")
            return number_of_guesses #Changed
            break
        elif computer_number > int(player_guess):
            print("Too low!")
        else:
            print("Too high!")

total_rounds = 0
total_guesses = 0 
while True:
    total_rounds = total_rounds + 1 #Added
    print("Starting round number: " + str(total_rounds)) #Changed
    print("Let the guessing begin!!")
    this_round = do_guess_round() #Changed
    
    #New if condition  (and code block) to test against quit
    if this_round == quit:
        total_rounds = total_rounds - 1
        avg = str(total_guesses/float(total_rounds))
        if total_rounds == 0:
            stats_message = 'You completed no rounds. ' + 'Please try again later.'
        else:
            stats_message = 'You played ' + str(total_rounds) + ' rounds, with an average of ' + str(avg)
            print(quit_message)
        break
    total_guesses = total_guesses + this_round
    avg = str(total_guesses/float(total_rounds))
    print("You took " + str(this_round)+" guesses")
    print("Your guessing average = " + str(avg))
    print("")
    
#Add exit messages
print(stats_message)