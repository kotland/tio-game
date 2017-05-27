import math
import random

field = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]

def check_input():
    while (True):
        position = input()
        try:
            if (int(position) < 10):
                break
        except:
            continue
    return position

def inputs():
    position = int(check_input())
    row = position / 3
    row = math.ceil(row)
    position = 2 - (row * 3 - position)
    if (field[row - 1][position] == " "):
        field[row - 1][position] = "X"
    else:
        inputs()

def print_field():
    for row in field:
        print(row)






while(True):

    inputs()
    print_field()
