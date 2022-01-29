import random
import matplotlib.pyplot as plot


def count(count_data, input_data):
    # check that the input data are all the same type
    if all(isinstance(item, type(input_data[0])) for item in input_data[1:]) == False:
        return -1  # we can't work with mixed lists
    # if count_data and input_data are strings, find how many of the individual
    # characters are in the input_data
    if type(count_data) == str and type(input_data) == str:
        counter = 0
        for letter in input_data:
            if letter in count_data:
                counter += 1
        return counter
    # if we have a list of two ints [a, b] and our input_data is also a list of ints
    # then count number of items in the range a to b
    elif type(count_data) == list and len(count_data) == 2 and type(count_data[0]) == int and type(input_data[0]) == int:
        counter = 0
        range_start = count_data[0]
        range_end = count_data[1]
        for item in input_data:
            if item >= range_start and item <= range_end:
                counter += 1
        return counter
    # if the type of count_data and the list elements of the input_data match
    # check to see how many matches we get
    elif type(count_data) == type(input_data[0]):
        counter = 0
        for item in input_data:
            if item == count_data:
                counter += 1
        return counter
    # else some error has occurred and we exit with -1
    else:
        return -1


scores = []
for x in range(0, 30):
    scores.append(random.randint(0, 10))
print(scores)

top_scorers = count(10, scores)  # Count function called here
print("{0} learners got top marks".format(top_scorers))

performance = []
for i in range(11):
    performance.append(count(i, scores))

plot.bar(range(11), performance, align='center', alpha=1)

plot.xticks(range(11))
plot.ylabel('Score frequency')
plot.title('Scores on a quiz')

plot.show()
plot.savefig(fname="Quiz Chart.png")
