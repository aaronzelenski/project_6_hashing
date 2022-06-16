import sys
import time
from time import perf_counter

PYRAMID_DEPTH = 23
global call_counter, cache_hits
call_counter = 0
cache_hits = 0

global dictionary
dictionary = {}
for i in range(0, PYRAMID_DEPTH):
    for j in range(0, PYRAMID_DEPTH + 1):
        dictionary[(i, j)] = -1.0


def weight_on_with_dict(r, c):
    weight_const = 200
    global call_counter, cache_hits, dictionary
    call_counter += 1

    if dictionary[(r, c)] != -1:
        cache_hits += 1
        return dictionary[(r, c)]

    # case 1 top of tree
    if r == 0 and c == 0:
        weight = 0.0
        dictionary[(r, c)] = weight
        return weight

    # case 2 left-hand side
    elif c == 0:
        weight = (weight_const + weight_on(r - 1, c)) / 2
        dictionary[(r, c)] = weight
        return weight

    # case 3 right_hand side
    elif r == c:
        weight = (weight_const + weight_on(r - 1, c - 1)) / 2
        dictionary[(r, c)] = weight
        return weight

    # case 4 everything else
    else:
        weight = (weight_const + weight_const + weight_on(r - 1, c-1) + weight_on(r-1, c)) / 2
        dictionary[(r, c)] = weight
        return weight


def weight_on(r, c):
    weight_const = 200
    global call_counter
    call_counter += 1

    # case 1 top of tree
    if r == 0 and c == 0:
        return 0.0

    # case 2 left-hand side
    elif c == 0:
        weight = (weight_const + weight_on(r - 1, c)) / 2
        return weight

    # case 3 right_hand side
    elif r == c:
        weight = (weight_const + weight_on(r - 1, c - 1)) / 2
        return weight

    # case 4 everything else
    else:
        weight = (weight_const + weight_const + weight_on(r - 1, c-1) + weight_on(r-1, c)) / 2
        return weight


def print_the_weight_calculations_with_dictionary():
    global call_counter, dictionary, cache_hits
    call_counter = 0
    cache_hits = 0

    for i in range(0, PYRAMID_DEPTH):
        print(" ")
        for j in range(0, i + 1):
            print(f" %6.2f" % (weight_on_with_dict(i, j)), end=" ")


def print_weight_pyramid():
    global call_counter, PYRAMID_DEPTH
    call_counter = 0
    for i in range(0, PYRAMID_DEPTH):
        print("")
        for j in range(0, i + 1):
            print(f" %.2f" % (weight_on(i, j)), end=" ")


def write_the_weight_calculations_to_a_file():
    global call_counter
    call_counter = 0
    f = open("part2.txt", "a")

    for i in range(0, PYRAMID_DEPTH):
        f.write("\n")
        for j in range(0, i + 1):
            f.write("{:6.2f} ".format(weight_on(i, j)))
    start = perf_counter()
    print_weight_pyramid()
    end = perf_counter()
    f.write(" ")
    f.write(f"\nElapsed time {end - start} seconds")
    f.write(f"\nNumber of function calls : {call_counter}")
    f.close()


def run_the_weight_calculations():
    global call_counter, cache_hits
    call_counter = 0
    cache_hits = 0
    for i in range(0, PYRAMID_DEPTH):
        for j in range(0, i + 1):
            if i == 0:
                pass
            if i == j:
                weight_on(i, j)
            if i != 0 and i != j:
                weight_on(i, j)


def run_the_weight_calculations_with_dictionary():
    global call_counter, cache_hits, dictionary
    call_counter = 0
    cache_hits = 0

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


start_timer = time.perf_counter()
run_the_weight_calculations_with_dictionary()
end_timer = time.perf_counter()
print_the_weight_calculations_with_dictionary()
elapsed_time = end_timer - start_timer
print()
print()
print(f"Elapsed time: {elapsed_time} seconds")
print(f"Function calls: {call_counter}")
print(f"Number of cache hits: {cache_hits}")
