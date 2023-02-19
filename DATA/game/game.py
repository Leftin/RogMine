import msvcrt
import os


def menu():
    run = True
    menu_punkt = ["New world", "Load world", "Setting", "Exit"]
    j = 0
    while run:
        os.system("cls")
        for i in range(len(menu_punkt)):
            print(menu_punkt[i], end="")
            if i==j:
                print("<--", end="")
            print()

        print("\n2 - next\n8 - back\n5 - ready")
        var = msvcrt.getch()
        if ord(var) == ord("2"):
            j += 1
        if ord(var) == ord("8"):
            j -= 1
        if ord(var) == ord("5"):
            if j == 0:
                run = False
            if j == 1:
                pass
            if j == 2:
                print("Soming soon")
            if j == 3:
                exit()

def pause():
    run = True
    pause_punkt = ["Play", "Setting", "Exit"]
    j = 0
    while run:
        os.system("cls")
        for i in range(len(pause_punkt)):
            print(pause_punkt[i], end="")
            if i==j:
                print("<--", end="")
            print()

        print("\n2 - next\n8 - back\n5 - ready")
        var = msvcrt.getch()
        if ord(var) == ord("2"):
            j += 1
        if ord(var) == ord("8"):
            j -= 1
        if ord(var) == ord("5"):
            if j == 0:
                run = False
            if j == 1:
                print("Soming soon")
            if j == 2:
                exit()
def setting():
    pass