import os
import time

def game_menu():
    os.system("clear")
    print("*________________________________________________________________________________________________________________________*")
    print("*     ██████╗  █████╗ ███╗   ███╗███████╗    ███████╗███████╗██╗     ███████╗ ██████╗████████╗██╗ ██████╗ ███╗   ██╗     *")
    print("*    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔════╝██╔════╝██║     ██╔════╝██╔════╝╚══██╔══╝██║██╔═══██╗████╗  ██║     *")
    print("*    ██║  ███╗███████║██╔████╔██║█████╗      ███████╗█████╗  ██║     █████╗  ██║        ██║   ██║██║   ██║██╔██╗ ██║     *")
    print("*    ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ╚════██║██╔══╝  ██║     ██╔══╝  ██║        ██║   ██║██║   ██║██║╚██╗██║     *")
    print("*    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ███████║███████╗███████╗███████╗╚██████╗   ██║   ██║╚██████╔╝██║ ╚████║     *")
    print("*     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝    ╚══════╝╚══════╝╚══════╝╚══════╝ ╚═════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝     *")
    print("*________________________________________________________________________________________________________________________*")
    print("*     -                                               [1] Worms                                                    +     *")
    print("*      -         x                                    [2] Guessing the number                        x            +      *")
    print("*       -         x                                   [3] Simon                                     x            +       *")
    print("*________________________________________________________________________________________________________________________*")

def option1():
    os.system("clear")
    from worm_menu import worm_menu
    worm_menu()

def option2():
    os.system("clear")
    from guessing_menu import guess_menu
    guess_menu()

def option3():
    os.system("clear")
    from simon_menu import simon_menu
    simon_menu()

game_menu()

try:
    option = int(input("Enter your option: "))
    if option == 1:
        option1()
        from worm_menu import worm_menu
        worm_menu()

    elif option == 2:
        option2()
        from guessing_menu import guess_menu
        guess_menu()
    elif option == 3:
        option3()
        from simon_menu import simon_menu
        simon_menu()

except ValueError:
    game_menu()
    print("NUMBERS ONLY!")
    time.sleep(3)

