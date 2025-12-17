import random


def main():

    level = get_level("Level: ")
    score = 0

    # Randomly generates ten (10) math problems formatted as X + Y = ,
    # No need to support operations other than addition (+).
    for _ in range(10):

        x = generate_integer(level)
        y = generate_integer(level)

        # allow the user up to three tries in total for that problem.
        for i in range(3):
            try:
                # Prompts the user to solve the problems.
                equation = int(input(f"{x} + {y} = "))
            except ValueError:
                print("EEE")
                if i == 2:
                    # after three tries, the program should output the correct answer.
                    print(f"{x} + {y} = {x + y}")
                continue
            # if an answer is not correct, the program should output EEE and prompt the user again.
            else:
                if equation == (x + y):
                    score += 1
                    break
                else:
                    print("EEE")
                    if i == 2:
                        # after three tries, the program should output the correct answer.
                        print(f"{x} + {y} = {x + y}")

    # The program should ultimately output the user’s score: the number of correct answers out of 10.
    print(f"Score: {score}/10")


# Prompts the user for a level
# If the user does not input 1, 2, or 3, the program should prompt again.
def get_level(prompt):
    while True:
        try:
            x = int(input(prompt))
        except ValueError:
            continue
        else:
            if 0 < x <= 3:
                return x
            else:
                continue


# Randomly generates X and Y as a non-negative integer with 𝑛 digits.
def generate_integer(level):
    number = random.choice(range(10 ** (level - 1), 10**level))
    return number


if __name__ == "__main__":
    main()
