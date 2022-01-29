highscore_file = "highscore.txt"


def maths_question(question, correct_answer):
    print(question, end="")
    while True:
        answer = input()
        try:
            answer = int(answer)
        except ValueError:
            print("Huh? What is your answer? ", end="")
        else:
            break
    if answer == correct_answer:
        print("Correctamundo!!")
        return 1
    else:
        print(f"Woops... the correct answer is {correct_answer}")
        return 0


def print_score(score):
    print("Your score is: ")
    print(f"---> {score} <---")
    print("\n")


try:
    print("The 10 highest scores previously were")
    with open(highscore_file, "r") as f:
        highscore = f.read()
        print(highscore)
except:
    print("Creating a new highscore.txt file")
    f = open(highscore_file, "w")
    f.close()

while True:
    scores = []
    names = []
    with open(highscore_file, "r") as file:
        for line in file:
            line = line.strip("\n")
            line = line.split(" ")
            names.append(line[0])
            scores.append(int(line[1]))

    score = 0

    print("\n\nWelcome to the Maths Quiz")
    print("Can you answer three questions and score maximum points?\n")
    name = input("What is your name? ")
    print("\n")

    score += maths_question("Question 1: What is the product of 2x2x2? ", 8)
    print_score(score)

    score += maths_question("Question 2: What is the factorial of 3? ", 6)
    print_score(score)

    score += maths_question("Question 3: What is the cubic root of 8? ", 2)
    print_score(score)

    position = 0
    for compare_score in scores:
        if score < compare_score:
            position += 1
    scores.insert(position, score)
    names.insert(position, name)

    scores = scores[:10]
    names = names[:10]

    print("HIGHSCORES")
    with open(highscore_file, "w") as file:
        for i in range(len(scores)):
            file.write(names[i] + " " + str(scores[i]) + "\n")
            print(names[i] + " " + str(scores[i]))
