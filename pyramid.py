import sys
import time


def weight_on(r, c):
    weight_const = 200

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


def main():
    pass


if __name__ == '__main__':
    main()
