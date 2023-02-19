import json
from os import system
import msvcrt

class class_craft():
    def __init__(self):
        pass

def crafting(hero: object, tcraft: object):
    run = True
    j = 0
    fi = open("DATA\items\items.json")
    json_filei = json.load(fi)
    while run:
        system("cls")
        for i in range(len(tcraft.craft)):
            for k in range(len(tcraft.craft[i])):
                print(json_filei["id"][tcraft.craft[i][k]].get("name"), end="")
                if k!=len(tcraft.craft[i])-1:
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
            # checking for workshop
            counter = 0
            if hasattr(tcraft, "need"):
                for k in range(len(tcraft.need)):
                    if tcraft.need[k] in hero.id_near:
                        counter += 1
            else:
                counter = 1
            if counter >= 1:
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
            else:
                print("Need a workshop")
                msvcrt.getch()
        elif ord(var) == ord("x"):
            run = False

def craft(hero, map):
    f = open("DATA\items\crafts.json")
    json_file = json.load(f)
    run = True
    i = 0
    f2 = open("DATA\items\items.json")
    json_file2 = json.load(f2)    
    f3 = open("DATA\map\cell.json")
    json_file3 = json.load(f3)    
    while run:
        system("cls")
        tcraft = class_craft()
        tcraft.name = json_file["crafts"][i].get("name")
        tcraft.craft = json_file["crafts"][i].get("craft")
        tcraft.result = json_file["crafts"][i].get("result")
        if "need" in json_file["crafts"][i]:
            tcraft.need = json_file["crafts"][i].get("need")
        


        print(f"Name: {tcraft.name}")
        if "need" in json_file["crafts"][i]:
            print("Need: ", end="")
            for j in range(len(tcraft.need)):
                print(json_file3["id"][tcraft.need[j]].get("name"), end="")
                if j!=len(tcraft.need)-1:
                    print(", ", end="")
            print()
        
        print("Crafts: ")
        for j in range(len(tcraft.craft)):
            print(f"{j+1}. ", end="")
            for k in range(len(tcraft.craft[j])):
                print(json_file2["id"][tcraft.craft[j][k]].get("name"), end="")
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
            crafting(hero, tcraft, map)
