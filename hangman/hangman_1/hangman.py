#TIP: use random.randint to get a random word from the list
import random


def read_file(file_name):
    """
    TODO: Step 1 - open file and read lines as words
    """
    open_file = open(file_name, "r")
    word_list = open_file.readlines()
    open_file.close()

    return word_list


def select_random_word(words):
    """
    TODO: Step 2 - select random word from list of file
    """
    word = words[random.randint(0, (len(words)-1))]
    guess_word = list(word)
    guess_word[random.randint(0, (len(guess_word)-2))] = "_"    
    guess_word = "".join(guess_word)

    print("Guess the word: {}".format(guess_word))

    return word


def get_user_input():
    """
    TODO: Step 3 - get user input for answer
    """

    return input("Guess the missing letter: ")


def run_game(file_name):
    """
    This is the main game code. You can leave it as is and only implement steps 1 to 3 as indicated above.
    """
    
    words = read_file(file_name)
    word = select_random_word(words)
    answer = get_user_input()

    print('The word was: '+word)


if __name__ == "__main__":
    run_game('short_words.txt')

