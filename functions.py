import random
from variables import *


def print_result(result_msg, result):
    print(f"{result_msg} {result}")


def print_message(msg):
    print(msg)


def roll_dice():
    input(start_message)
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    roll = die1 + die2
    return roll


def continue_game():
    while True:
        question = input(continue_question).upper()
        if question == 'N':
            print_message(exit_message)
            return False
        elif question == 'Y':
            return True
        else:
            print_message(invalid_input_message)


def play_craps():
    while True:
        roll_sum = roll_dice()
        if roll_sum == 7 or roll_sum == 11:
            print_result(result_message, roll_sum)
            print_message(win_message)

        elif roll_sum == 2 or roll_sum == 3 or roll_sum == 12:
            print_result(result_message, roll_sum)
            print_message(lose_message)

        else:
            new_goal = roll_sum
            print_result(new_goal_message, new_goal)
            while True:
                new_roll = roll_dice()
                if new_roll == new_goal:
                    print_result(result_message, new_roll)
                    print_message(win_message)
                    break
                elif new_roll == 7:
                    print_result(result_message, new_roll)
                    print_message(lose_message)
                    break
                else:
                    print_result(result_message, new_roll)
                    print_message(continue_message)
        if not continue_game():
            return
