import math
import random

field = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]
#test_fields[Number of cases][0 - field \ 1 - result]
test_fields = [
[[["X", "O", " "],
  [" ", "O", " "],
  [" ", "O", "X"]], "O win!"],

[[[" ", "O", " "],
  ["X", "X", "X"],
  [" ", "O", " "]], "X win!"],
[[["O", " ", "X"],
  ["O", "X", " "],
  ["O", " ", "X"]], "O win!"],

[[[" ", " ", "O"],
  [" ", "O", "O"],
  ["X", "X", "X"]], "X win!"],

[[["X", "O", "O"],
  [" ", "X", " "],
  [" ", "O", "X"]], "X win!"],

[[["X", "X", "O"],
  ["X", "O", " "],
  ["O", " ", " "]], "O win!"]
]
def check_input(position):
    try:
        val = int(position)
        if (val < 10 and val > 0):
            return 0
    except:
        return -1
    return -1

def user_turn(field):
    print("user_turn:")
    while (True):
        val = input()
        if(check_input(val) < 0):
            continue
        if(user_input(int(val), field) < 0):
            continue
        break

def user_input(position, field):
    row = position / 3
    row = math.ceil(row)
    position = position - row * 3 - 1
    if (field[row - 1][position] == " "):
        field[row - 1][position] = "X"
        return 0
    else:
        return -1

def print_field(field):
    for row in field:
        print(row)

def computer_turn(field):
    while(True):
        row = random.randint(0, 2)
        pos = random.randint(0, 2)
        if (field[row][pos] == " "):
            field[row][pos] = "O"
            break
        else:
            continue

def check_win(field):
    win = ""
    for row in range(0, 3):
        if (field[row][0] == field[row][1] == field[row][2] != " "):
            win = field[row][0].__str__() + " win!"

    for col in range(0, 3):
        if (field[0][col] == field[1][col] == field[2][col] != " "):
            win = field[0][col].__str__() + " win!"

    if (field[0][0] == field[1][1] == field[2][2] != " "):
        win = field[0][0].__str__() + " win!"

    if (field[0][2] == field[1][1] == field[2][0] != " "):
        win = field[0][2].__str__() + " win!"

    return win

def test():
    print("Testing")
    for case in test_fields:
        print_test(case)
        if (case[1] != check_win(case[0])):
            print("check_win:\t[FAIL]")
    print("check_win:\t[OK]")

def print_test(test_field):
    print_field(test_field[0])
    print(test_field[1], "? ", "True" if test_field[1] == check_win(test_field[0]) else "False")

def main():
    print("Welcome to Tic-Tac-Toe")
    print("Input 1 to test, 2 to play game")
    var = input()
    try:
        var = int(var)

        if (var == 1):
            test()
        elif (var == 2):
            game_field = field
            while(True):
                user_turn(game_field)
                computer_turn(game_field)
                print_field(game_field)
                result = check_win(game_field)
                if (result != ""):
                    print(result)
                    break
        else:
            print("Wrong input")
    except:
        print("Wrong input")


main()