import random
import sys

def read_file(file_name):
    file = open(file_name,'r')
    return file.readlines()


def get_user_input():
    return input('Guess the missing letter: ')


def ask_file_name():
    try:
        file_name = str(sys.argv[1])
    except IndexError:
        file_name = ""
    if not file_name:
        return 'short_words.txt'
    return file_name


def select_random_word(words):
    random_index = random.randint(0, len(words)-1)
    word = words[random_index].strip()
    return word


# TODO: Step 1 - update to randomly fill in one character of the word only
def random_fill_word(word):
    guess_word = list("_"*len(word))
    random_let_index = random.randint(0, len(word)-1)
    guess_word[random_let_index] = word[random_let_index]
    return "".join(guess_word)


# TODO: Step 1 - update to check if character is one of the missing characters
def is_missing_char(original_word, answer_word, char):
    if answer_word.count(char) == original_word.count(char):
        return False
    elif char in original_word:
        return True
    
    return False


# TODO: Step 1 - fill in missing char in word and return new more complete word
def fill_in_char(original_word, answer_word, char):
    new_answer_word = list(answer_word)
    for i,j in enumerate(original_word):
        if  j == char:
            new_answer_word[i] = char
    return "".join(new_answer_word)


def do_correct_answer(original_word, answer, guess):
    answer = fill_in_char(original_word, answer, guess)
    print(answer)
    return answer


# TODO: Step 4: update to use number of remaining guesses
def do_wrong_answer(answer, number_guesses):
    print('Wrong! Number of guesses left: '+str(number_guesses))
    draw_figure(number_guesses)


# TODO: Step 5: draw hangman stick figure, based on number of guesses remaining
def draw_figure(number_guesses):
    if number_guesses == 4:
        print("/----\n|\n|\n|\n|\n_______")
    elif number_guesses == 3:
        print("/----\n|   0\n|\n|\n|\n_______")
    elif number_guesses == 2:
        print("/----\n|   0\n|  /|\\\n|\n|\n_______")
    elif number_guesses == 1:
        print("/----\n|   0\n|  /|\\\n|   |\n|\n_______")
    elif number_guesses == 0:
        print("/----\n|   0\n|  /|\\\n|   |\n|  / \\\n_______")

# TODO: Step 2 - update to loop over getting input and checking until whole word guessed
# TODO: Step 3 - update loop to exit game if user types `exit` or `quit`
# TODO: Step 4 - keep track of number of remaining guesses
def run_game_loop(word, answer):

    guesses = 5
    print("Guess the word: "+answer)

    while True:
        
        if guesses == 0:
            print('Sorry, you are out of guesses. The word was: '+word)
            break
        elif answer == word:
            break

        guess = get_user_input()

        if guess.lower() == "exit" or guess.lower() == "quit":
            print('Bye!')
            break
        elif is_missing_char(word, answer, guess):
            answer = do_correct_answer(word, answer, guess)
        else:
            guesses -= 1
            do_wrong_answer(answer, guesses)
            


# TODO: Step 6 - update to get words_file to use from commandline argument
if __name__ == "__main__":
    words_file = ask_file_name()
    words = read_file(words_file)
    selected_word = select_random_word(words)
    current_answer = random_fill_word(selected_word)

    run_game_loop(selected_word, current_answer)

