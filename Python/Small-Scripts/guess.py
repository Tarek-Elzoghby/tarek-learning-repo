import random

def main():
    level = get_postive("Level: ")

    number = random.choice(range(1, level + 1))

    
    while True:
        user_guess = get_postive("Guess: ")
        if user_guess < number:
            print("Too small!")
        elif user_guess > number:
            print("Too large!")
        else:
            print("Just right!")
            break





def get_postive(prompt):
    while True:
        try:
            x = int(input(prompt))
        except ValueError:
            continue
        else:
            if x > 0 :
                return x
            else:
                continue


main()