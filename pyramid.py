import sys
import time
from time import perf_counter

pyramid_depth = 7
call_counter = 0

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


def print_weight_pyramid():
    global pyramid_depth
    start_timer = time.perf_counter()
    for i in range(0, pyramid_depth):
        print("")
        for j in range(0, i + 1):
            print(f" %.2f" % (weight_on(i, j)), end=" ")
    end_timer = time.perf_counter()
    elapsed_time = end_timer - start_timer
    print()
    print()
    print(f"Elapsed time: {elapsed_time} seconds")
    print(f"Function calls: {call_counter}")


if __name__ == '__main__':
    if len(sys.argv) != 1:
        PYRAMID_DEPTH = int(sys.argv[1])

