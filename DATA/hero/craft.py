import json
from os import system
import msvcrt

class class_craft():
    def __init__(self):
        pass

def crafting(hero, tcraft):
    run = True
    j = 0
    fi = open("DATA\items\items.json")
    json_filei = json.load(fi)
    while run:
        system("cls")
        for i in range(len(tcraft.craft)):
            for k in range(len(tcraft.craft[j])):
                print(json_filei["id"][tcraft.craft[i][k]].get("name"), end="")
                if k!=len(tcraft.craft[j])-1:
                    print(", ", end="")
            if i == j:
                print(f" <--", end="")
            print()
        print("\n2 - next\n8 - back\n5 - ready\n\nx - cancel")
        var = msvcrt.getch()
        if ord(var) == ord("2"):
            if j < len(tcraft.craft):
                j += 1
        elif ord(var) == ord("8"):
            if j > 0:
                j -= 1
        elif ord(var) == ord("5"):
            # checking for resources
            counter = 0
            for k in range(len(tcraft.craft[j])):
                for a in range(len(hero.inventory)):
                    if hero.inventory[a].id == tcraft.craft[j][k]:
                        counter += 1
                        break
            if counter == len(tcraft.craft[j]):
                # deleting resources
                for k in range(len(tcraft.craft[j])):
                    for a in range(len(hero.inventory)):
                        if hero.inventory[a].id == tcraft.craft[j][k]:
                            hero.inventory[a].id = 0
                            break
                # get resources
                hero.get_resourse(tcraft.result)
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
    fi = open("DATA\items\items.json")
    json_filei = json.load(fi)    
    while run:
        system("cls")
        tcraft = class_craft()
        tcraft.name = json_file["crafts"][i].get("name")
        tcraft.craft = json_file["crafts"][i].get("craft")
        tcraft.result = json_file["crafts"][i].get("result")
        


        print(f"Name: {tcraft.name}")
        print("Crafts: ")
        for j in range(len(tcraft.craft)):
            print(f"{j+1}. ", end="")
            for k in range(len(tcraft.craft[j])):
                print(json_filei["id"][tcraft.craft[j][k]].get("name"), end="")
                if k!=len(tcraft.craft[j])-1:
                    print(", ", end="")
            print()
        print("\n6 - next\n4 - back\n5 - ready\n\nx - cancel")
        var = msvcrt.getch()
        if ord(var) == ord("6"):
            if i < len(json_file["crafts"])-1:
                i += 1
        if ord(var) == ord("4"):
            if i > 0:
                i -= 1
        if ord(var) == ord("x"):
            run = False   
        if ord(var) == ord("5"):
            crafting(hero, tcraft)