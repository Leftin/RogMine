import DATA.map.map
import random
import json

class world():
    def __init__(self, worldX, worldY, mapX, mapY):
        self.board = list()
        self.x = worldX
        self.y = worldY
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