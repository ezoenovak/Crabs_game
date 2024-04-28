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
        for sublist in roll_options:
            if roll_sum in sublist:
                print_result(result_message, roll_sum)
                if sublist == roll_options[0]:
                    print_message(win_message)
                else:
                    print_message(lose_message)
                break

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
