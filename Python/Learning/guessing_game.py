# Guessing Game

max = 101
min = 0


def guess_number(min, max):
    answer = ""
    no_of_guesses = 0
    while answer != "S":
        no_of_guesses += 1
        middle = int((min + max)/2)
        answer = input(
            f"Is your number [H]igher, [L]ower or the [S]ame as {middle} -> ").upper()
        if answer == "H":
            min = middle
        elif answer == "L":
            max = middle
    return middle, no_of_guesses


print("Think of a number between 1 and 100")
number, no_of_guesses = guess_number(min, max)

print(f"Your number is {number}, it took me {no_of_guesses} guesses.")
