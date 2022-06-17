"""file holds all pyramid functions"""
import sys
from time import perf_counter
from HashMap import HashMap

PYRAMID_DEPTH = 7
global CALL_COUNTER, CACHE_HITS
CALL_COUNTER = 0
CACHE_HITS = 0

global DICTIONARY
DICTIONARY = {}


def weight_on_with_dict(row, column):
    """routine used to calculate the weight on each individual using dictionary"""

    weight_const = 200
    global CALL_COUNTER, CACHE_HITS, DICTIONARY
    CALL_COUNTER += 1

    if DICTIONARY[(row, column)] != -1:
        CACHE_HITS += 1
        return DICTIONARY[(row, column)]

    # case 1 top of tree
    if row == 0 and column == 0:
        weight = 0.0
        DICTIONARY[(row, column)] = weight
        return weight

    # case 2 left-hand side
    if column == 0:
        weight = (weight_const + weight_on_with_dict(row - 1, column)) / 2
        DICTIONARY[(row, column)] = weight
        return weight

    # case 3 right_hand side
    if row == column:
        weight = (weight_const + weight_on_with_dict(row - 1, column - 1)) / 2
        DICTIONARY[(row, column)] = weight
        return weight

    # case 4 everything else
    weight = (weight_const + weight_const + weight_on_with_dict(row - 1, column - 1)
              + weight_on_with_dict(row - 1, column)) / 2
    DICTIONARY[(row, column)] = weight
    return weight


def weight_on(row, column):
    """routine used to calculate the weight on each individual"""
    weight_const = 200
    global CALL_COUNTER
    CALL_COUNTER += 1

    # case 1 top of tree
    if row == 0 and column == 0:
        return 0.0

    # case 2 left-hand side
    if column == 0:
        weight = (weight_const + weight_on(row - 1, column)) / 2
        return weight

    # case 3 right_hand side
    if row == column:
        weight = (weight_const + weight_on(row - 1, column - 1)) / 2
        return weight

    # case 4 everything else
    weight = (weight_const + weight_const + weight_on(row - 1, column - 1)
              + weight_on(row - 1, column)) / 2
    return weight


def print_the_weight_pyramid_with_dictionary():
    """print weight pyramid using dictionary"""
    global CALL_COUNTER, DICTIONARY, CACHE_HITS
    CALL_COUNTER = 0
    CACHE_HITS = 0

    for i in range(0, PYRAMID_DEPTH):
        for j in range(0, PYRAMID_DEPTH + 1):
            DICTIONARY[(i, j)] = -1.0

    for i in range(0, PYRAMID_DEPTH):
        print(" ")
        for j in range(0, i + 1):
            print(f" %6.2f" % (weight_on_with_dict(i, j)), end=" ")


def print_weight_pyramid():
    """print weight pyramid """
    global CALL_COUNTER, PYRAMID_DEPTH
    CALL_COUNTER = 0
    for i in range(0, PYRAMID_DEPTH):
        print("")
        for j in range(0, i + 1):
            print(f" %.2f" % (weight_on(i, j)), end=" ")


def write_the_weight_calculations_to_a_file():
    """writing the pyramid to part2.txt file"""
    global CALL_COUNTER
    CALL_COUNTER = 0
    file = open("part2.txt", "a")

    for i in range(0, PYRAMID_DEPTH):
        file.write("\n")
        for j in range(0, i + 1):
            file.write("{:6.2f} ".format(weight_on(i, j)))
    start = perf_counter()
    print_the_weight_pyramid_with_dictionary()
    end = perf_counter()
    file.write(" ")
    file.write(f"\nElapsed time {end - start} seconds")
    file.write(f"\nNumber of function calls : {CALL_COUNTER}")
    file.write(f"\nNumber of cache hits : {CACHE_HITS}")
    file.close()


def run_the_weight_calculations():
    """weight calc not using dict"""
    for i in range(0, PYRAMID_DEPTH):
        for j in range(0, PYRAMID_DEPTH + 1):
            DICTIONARY[(i, j)] = -1.0

    global CALL_COUNTER, CACHE_HITS
    CALL_COUNTER = 0
    CACHE_HITS = 0
    for i in range(0, PYRAMID_DEPTH):
        for j in range(0, i + 1):
            if i == 0:
                pass
            if i == j:
                weight_on(i, j)
            if i != 0 and i != j:
                weight_on(i, j)


def run_the_weight_calculations_with_dictionary():
    """weight calc using dict"""
    global CALL_COUNTER, CACHE_HITS, DICTIONARY
    for i in range(0, PYRAMID_DEPTH):
        for j in range(0, PYRAMID_DEPTH + 1):
            DICTIONARY[(i, j)] = -1.0
    CALL_COUNTER = 0
    CACHE_HITS = 0

    for i in range(0, PYRAMID_DEPTH):
        for j in range(0, i + 1):
            if i == 0:
                pass
            if i == j:
                weight_on_with_dict(i, j)
            if i != 0 and i != j:
                weight_on_with_dict(i, j)


if __name__ == '__main__':
    if len(sys.argv) != 1:
        PYRAMID_DEPTH = int(sys.argv[1])

MyHashMap = HashMap

write_the_weight_calculations_to_a_file()
