import json
from os import system
import msvcrt

class class_craft():
    def __init__(self):
        pass

def crafting(hero, tcraft):
    run = True
    j = 0
    while run:
        system("cls")
        for i in range(len(tcraft.craft)):
            if i == j:
                print(f"{i}. {tcraft.craft[i]} <--")
            else:
                print(f"{i}. {tcraft.craft[i]}")
        var = msvcrt.getch()
        if ord(var) == ord("2"):
            j += 1
        elif ord(var) == ord("8"):
            j -= 1
        elif ord(var) == ord("5"):
            counter = 0
            for k in range(len(tcraft.craft[j])):
                for a in range(len(hero.inventory)):
                    if hero.inventory[a].id == tcraft.craft[j][k]:
                        counter += 1
                        break
            if counter == len(tcraft.craft[j]):
                for k in range(len(tcraft.craft[j])):
                    for a in range(len(hero.inventory)):
                        if hero.inventory[a].id == tcraft.craft[j][k]:
                            hero.inventory[a].id = 0
                            break
                        
                for j in range(len(hero.inventory)):
                    if hero.inventory[j].id == 0:
                        hero.inventory[j].id = tcraft.result
                        break
            else:
                print("Need More Resourses!")
                msvcrt.getch()
            run = False
        elif ord(var) == ord("x"):
            run = False

def craft(hero):
    f = open("DATA\items\crafts.json")
    json_file = json.load(f)



    run = True
    i = 0
    while run:
        system("cls")
        tcraft = class_craft()
        tcraft.name = json_file["crafts"][i].get("name")
        tcraft.craft = json_file["crafts"][i].get("craft")
        tcraft.result = json_file["crafts"][i].get("result")
        
        f = open("DATA\items\items.json")
        json_file = json.load(f)

        print(f"Name: {tcraft.name}")
        print("Crafts: ")
        for j in range(len(tcraft.craft)):
            print(f"{j}. ", end="")
            for k in range(len(tcraft.craft[j])):
                print(json_file["id"][tcraft.craft[j][k]].get("name"), end=", ")
            print()
        var = msvcrt.getch()
        if ord(var) == ord("6"):
            i += 1
        if ord(var) == ord("4"):
            i -= 1
        if ord(var) == ord("x"):
            run = False   
        if ord(var) == ord("5"):
            crafting(hero, tcraft)
        f = open("DATA\items\crafts.json")
        json_file = json.load(f)