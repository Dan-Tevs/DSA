import os
import time

def menu():
    os.system("clear")
    print("***************************************************************")
    print("*            ███╗   ███╗███████╗███╗   ██╗██╗   ██╗           *")
    print("*            ████╗ ████║██╔════╝████╗  ██║██║   ██║           *")
    print("*            ██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║           *")
    print("*            ██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║           *")
    print("*            ██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝           *")
    print("*            ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝            *")
    print("*                         [1] Menu                            *")
    print("*                         [2] About                           *")
    print("*                         [3] Exit                            *")
    print("***************************************************************")

def option1():
    os.system("clear")
    from gameMenu import game_menu
    game_menu()
    

def option2():
    os.system("clear")
    print("*****************************************************************************************************")
    print("*                            █████╗ ██████╗  ██████╗ ██╗   ██╗████████╗                             *")
    print("*                           ██╔══██╗██╔══██╗██╔═══██╗██║   ██║╚══██╔══╝                             *")
    print("*                           ███████║██████╔╝██║   ██║██║   ██║   ██║                                *")
    print("*                           ██╔══██║██╔══██╗██║   ██║██║   ██║   ██║                                *")
    print("*                           ██║  ██║██████╔╝╚██████╔╝╚██████╔╝   ██║                                *")
    print("*                           ╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚═════╝    ╚═╝                                *")
    print("*        This game is our Project. Our goal is to implementing Stack, Queue, and Linked List game.  *")
    print("*****************************************************************************************************")

    user = input("Enter 'e' to exit: ")
    if user == 'e':
        menu()

def option3():
    print("Program Terminated. Thank You!")

menu()

try:
    option = int(input("Enter your option: "))
    if option == 1:
        option1()
    elif option == 2:
        option2()
    elif option == 3:
        option3()
    is_exit = False

except ValueError:
    menu()
    print("NUMBERS ONLY!")
    time.sleep(3)