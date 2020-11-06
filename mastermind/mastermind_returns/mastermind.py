import random


def create_code():
    """
    creates a list of 4 none repeating digits
    in range 1 - 8
    Returns:
        list: codelist
    """
    codelist = set()

    while len(codelist) < 4:
        codelist.add(random.randint(1, 8))

    return list(codelist)


def get_answer_input():
    """
    get user input
    Returns:
        list: list of user input
    """
    answer = input("Input 4 digit code: ")
    is_valid = False

    while is_valid != True:
        if len(answer) != 4 or answer.isdigit() != True or "0" in answer or "9" in answer:
            print("Please enter exactly 4 digits.")
            answer = input("Input 4 digit code: ")
            continue
        is_valid = True

    return [int(i) for i in answer]


def show_instructions():
    """
    prints instructions
    """
    print('4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.')


def show_results(correct_digits_and_position,correct_digits_only):
    """
    prints results correct digits and correct digits in correct place
    Args:
        correct_digits_and_position (int): number of correct digits in position
        correct_digits_only (int): number of correct digits only
    """
    print('Number of correct digits in correct place:     ' + str(correct_digits_and_position))
    print('Number of correct digits not in correct place: ' + str(correct_digits_only))


def take_turn(code):
    """Handle the logic of taking a turn, which includes:
       * get answer from user
       * check if answer is valid
       * check correctness of answer
    """
    answer = get_answer_input()
    correct_digits_and_position = 0
    correct_digits_only = 0

    for i in range(len(answer)):
        if code[i] == int(answer[i]):
            correct_digits_and_position += 1
        elif int(answer[i]) in code:
            correct_digits_only += 1
    show_results(correct_digits_and_position,correct_digits_only)

    return  (correct_digits_and_position, correct_digits_only)


def show_code(code):
    """Show Code that was created to user"""
    print('The code was: '+str(code))


def check_correctness(turns, correct_digits_and_position):
    """checks if all digits in correct possition prints result
    Args:
        turns (int): current turns
        correct_digits_and_position (int): number of correct digits in correct place
    Returns:
        bool: True, if all correct else False.
    """
    if correct_digits_and_position == 4:
        print('Congratulations! You are a codebreaker!')
        return True
    else:
        print('Turns left: ' + str(12 - turns))
        return False


def run_game():
    """Main function for running the game"""
    correct_digits_and_position = 0
    correct = False
    code = create_code()
    
    show_instructions()

    turns = 0
    while not correct and turns < 12:
        correct_tuple  = take_turn(code)
        correct_digits_and_position = correct_tuple[0]
        turns += 1
        correct = check_correctness(turns,correct_digits_and_position)

    show_code(code)


if __name__ == "__main__":
    run_game()
