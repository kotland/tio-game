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

def computers():
    while(True):
        row = random.randint(0, 2)
        pos = random.randint(0, 2)
        if (field[row][pos] == " "):
            field[row][pos] = "O"
            break
        else:
            continue

def check_win():
    for row in range(0, 2):
        if (field[row][0] == field[row][1] == field[row][2] != " "):
            print(field[row][0].__str__() + " win!")
            exit()

    for cel in range(0, 2):
        if (field[0][cel] == field[1][cel] == field[2][cel] != " "):
            print(field[row][0].__str__() + " win!")
            exit()



while(True):

    inputs()
    computers()
    print_field()
    check_win()
