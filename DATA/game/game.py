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

def pause(hero):
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
                j = 0
                run2 = True
                while run2:
                    setting_punkt = ["Exit", f"Mode: {hero.mode}", f"Hero texture: {hero.texture}", f"Update method: {hero.update_method}", f"Show coordinates: {hero.show_coordinates}"]
                    os.system("cls")
                    for i in range(len(setting_punkt)):
                        print(setting_punkt[i], end="")
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
                            run2 = False
                            j = 0
                        if j == 1:
                            new_mode = input("Set new value")
                            if len(new_mode) > 0:
                                hero.mode = int(new_mode)
                        if j == 2:
                            new_texture = input("Set new value")
                            if len(new_texture) > 0:
                                hero.texture = new_texture[0]
                        if j == 3:
                            new_update = input("Set new value")
                            if len(new_update) > 0:
                                hero.update_method = int(new_update)
                        if j == 4:
                            if hero.show_coordinates == True: hero.show_coordinates = False
                            else: hero.show_coordinates = True
                    
                

            if j == 2:
                exit()
def setting():
    pass