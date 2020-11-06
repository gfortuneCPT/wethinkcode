import random
from typing import Counter


def  gen_code():
    """
    Generates Secret Code.
        :returns: List of 4 integers
    """
    codelist = set()

    while len(codelist) < 4:
        codelist.add(random.randint(1, 8))

    return list(codelist)


def get_valid_user_input():
    """
    Gets then validates user guess
        :returns: List of integers of user input
    """
    guess = input("Input 4 digit code: ")
    is_valid = False

    while is_valid != True:
        if len(guess) != 4 or guess.isdigit() != True or "0" in guess or "9" in guess:
            print("Please enter exactly 4 digits.")
            guess = input("Input 4 digit code: ")
            continue
        is_valid = True

    return [int(i) for i in guess]


def check_correct(user_input, secret_code):
    """
    Counts correct guesses and guesses with correct positions 
    in the code.

    :user_input: user guess
    :secret_code: the correct code

    :returns: list of 2 int values 
        counter[0] contains number of correct letters not in correct place
        counter[1] contains number of correct letters in correct place
    """
    counter = [0,0]

    for i in user_input:
        if i in secret_code:
            counter[0] += 1
            if user_input.index(i) == secret_code.index(i):
                counter[1] += 1
                counter[0] -= 1

    return counter


def run_game():
    """
    main game loop
    """
    #Step:  1
    code = gen_code()
    print("4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.")
    
    #Step:  2
    turns_left = 11
    while True:
        guess = get_valid_user_input()

    #Step : 3,4
        count = check_correct(guess,code)
        
        print("Number of correct digits in correct place:     {}".format(count[1]))
        print("Number of correct digits not in correct place: {}".format(count[0]))

        if count[1] != 4:
            print("Turns left: {}".format(turns_left))
            turns_left -=1
        elif turns_left == 0:
            break
        else:
            print("Congratulations! You are a codebreaker!\nThe code was: "+str(code))
            break      
    
if __name__ == "__main__":
    run_game()
