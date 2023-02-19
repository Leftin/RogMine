import DATA.map.map
import random
import json
import msvcrt
import os
import shutil

class world():
    def __init__(self, worldX: int, worldY: int, mapX: int, mapY: int):
        self.board = list()
        self.clock = 0
        self.x = worldX
        self.y = worldY
        print("Generate world...")
        for i in range(self.y):
            self.board.append(list())
            for j in range(self.x):
                self.board[i].append(DATA.map.map.map(mapX, mapY)) 
                self.board[i][j].generation()
    def write(self):
        for i in range(self.y):
            for j in range(self.x):
                print(self.board[i][j].texture, end="")
            print()
    def generation(self):
        f = open("DATA\map\cell.json")
        json_file = json.load(f)
        for i in range(len(json_file["id"])):
            if "world_count" in json_file["id"][i]:
                count = json_file["id"][i].get("world_count") + random.randint(-3, 3)
                for j in range(count):
                    self.board[random.randint(0, self.y-1)][random.randint(0, self.x-1)].board[random.randint(0, self.y-1)][random.randint(0, self.x-1)].id = i 

    def update(self):
        for i in range(self.y):
            for j in range(self.x):
                self.board[i][j].update()
    
    def save(self):
        num = 0
        run = True
        while run:
            world.name = input("Set name your map: ")
            if len(self.name) > 0:
                run = False
            else:
                print("You can't leave your will empty!")
        if os.path.exists(f"DATA\saves\\{self.name}"):
            shutil.rmtree(f"DATA\saves\\{self.name}")
        os.mkdir(f"DATA\saves\\{self.name}")
        for i in range(self.y):
            for j in range(self.x):
                self.board[i][j].save(self.name, num)
                num += 1
        print("World saved!")
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
            num = 0
            for i in range(self.y):
                for j in range(self.x):
                    self.board[i][j].load(self.name, num)
                    num += 1
            print("World load!")
            msvcrt.getch()