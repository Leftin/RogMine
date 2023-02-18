import DATA.map.cell
import random
import json
import msvcrt
import os
import shutil
import DATA.game.game
import math
import collections

class map():
    def __init__(self, mapX, mapY):
        self.x = mapX
        self.y = mapY
        self.alert = ""
        self.clock_alert = 0
        self.hold_alert = 1
        self.centr_x = math.floor(self.x/2)
        self.clock = 0
        self.texture = "."
        self.board = list()
        
        for i in range(self.y):
            self.board.append(list())
            for j in range(self.x):
                self.board[i].append(DATA.map.cell.cell()) 
    def write(self):
        for i in range(self.y):
            for j in range(self.x):
                print(self.board[i][j].texture, end="")
            print()

        for i in range(self.centr_x):    
            print(" ", end="")
        print(self.alert)
    def update(self):
        for i in range(self.y):
            for j in range(self.x):
                self.board[i][j].update()  
        if self.clock_alert == self.hold_alert:
            self.alert = ""
            self.clock_alert = 0
        if len(self.alert) > 0:
            self.clock_alert += 1
    def generation(self):
        f = open("DATA\map\cell.json")
        json_file = json.load(f)
        for i in range(len(json_file["id"])):
            if "count" in json_file["id"][i]:
                count = json_file["id"][i].get("count")
                if i == 1 or i == 2:
                    count += random.randint(-3, 3)
                for j in range(count):
                    self.board[random.randint(0, self.y-1)][random.randint(0, self.x-1)].id = i 
    def save(self):
        run = True
        while run:
            self.name = input("Set name your map: ")
            if len(self.name) > 0:
                run = False
            else:
                print("You can't leave your will empty!")
        if os.path.exists(f"DATA\saves\\{self.name}"):
            shutil.rmtree(f"DATA\saves\\{self.name}")
        os.mkdir(f"DATA\saves\\{self.name}")
        f = open(f"DATA\saves\\{self.name}\map.json", "w")
        save_map = list()
        k = 0
        for i in range(self.y):
            for j in range(self.x):
                save_map.append(list())
                save_map[k].append(self.board[i][j].id)
                k += 1
        json.dump(save_map, f)
        print("Map saved!")
        msvcrt.getch()
    def load(self):
        run = True
        j = 0
        saves = os.listdir("DATA\saves")
        while run:
            os.system("cls")
            print("══════")
            for i in range(len(saves)):
                if i == j:
                    print(f"{i+1}. {saves[i]} <--")
                else:
                    print(f"{i+1}. {saves[i]}")
            print("══════")
            print("\n2 - next\n8 - back\n5 - ready\n\nx - cancel")
            var = msvcrt.getch()
            if ord(var) == ord("2"):
                j += 1
            if ord(var) == ord("8"):
                j -= 1
            if ord(var) == ord("x"):
                run = False
                run2 = False
                return 1
            if ord(var) == ord("5"):
                self.name = saves[j]
                run = False
                run2 = True
        if run2:
            f = open(f"DATA\saves\\{self.name}\map.json", "r")
            load_map = json.load(f)
            k = 0
            for i in range(self.y):
                for j in range(self.x):
                    self.board[i][j].id = load_map[k][0]
                    k += 1
            os.system("cls")
            self.write()
            print("Map loaded!")
            msvcrt.getch()
    def pause(self):
        DATA.game.game.pause()
    def update_texture(self):
        textures = list()
        for i in range(self.y):
            for j in range(self.x):
                textures.append(self.board[i][j].id)
        a = textures.count(2)
        b = textures.count(1)
        c = textures.count(10)
        if a > b:
            self.texture = "#"
        elif a < b:
            self.texture = "T"
        elif c >= 1:
            self.texture = "V"
        else:
            self.texture = " "