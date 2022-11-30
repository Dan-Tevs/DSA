import os
import time
import sys
import random

def simon():
    numbers_to_generate_from = list(range(0,11)) # 0 1 2 3 4 5 6 7 8 9 10
    simon_questions_amount = 10

    simon_says_list = []
    for question in range(simon_questions_amount):
        chosen_number = random.choice(numbers_to_generate_from)
        simon_says_list.append(chosen_number)

        print("There are the numbers you have to memorize: {0}".format(simon_says_list))
        time.sleep(3)

        os.system("clear")

        for num in simon_says_list:
            user_answer = int(input("Im Simon. Please type the numbers, press enter after each number: "))

            if user_answer == num:
                print("Well done, Keep going!")
                continue

            else:
                print("You did not get the correct number, Game Over!")
                print("Your Score is {0}".format(question))
                sys.exit()