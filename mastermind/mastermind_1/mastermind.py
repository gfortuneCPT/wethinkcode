import random

def run_game():
    #Step:  1
    codelist = set()
    while len(codelist) < 4:
        codelist.add(random.randint(1, 8))
    code = list(codelist)
    print("4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.")
    #print(code)

    #Step:  2
    turns_left = 11
    while True:
        guess = input("Input 4 digit code: ")
        is_valid = False
        while is_valid != True:
            if len(guess) != 4 or guess.isdigit() != True or "0" in guess or "9" in guess:
                print("Please enter exactly 4 digits.")
                guess = input("Input 4 digit code: ")
                continue
            is_valid = True
        guess = [int(i) for i in guess]

    #Step : 3,4
        count = [0,0]
        for i in guess:
           if i in code:
                count[0] += 1
                if guess.index(i) == code.index(i):
                    count[1] += 1
                    count[0] -= 1
        
        print("Number of correct digits in correct place:     {}".format(count[1]))
        print("Number of correct digits not in correct place: {}".format(count[0]))
        if count[1] != 4:
            print("Turns left: {}".format(turns_left))
            turns_left -=1
        elif turns_left == 0:
            break
        else:
            code = "".join(map(str, code))
            print("Congratulations! You are a codebreaker!\nThe code was: "+str(code))
            break      
    pass
if __name__ == "__main__":
    run_game()
