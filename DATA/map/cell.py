import json
import random

class cell():
    def __init__(self):
        self.id = 0
        self.idc = 0
        f = open("DATA\map\cell.json")
        json_file = json.load(f)
        self.drop = json_file["id"][self.id].get("drop")
    
    def update(self):
        f = open("DATA\map\cell.json")
        json_file = json.load(f)
        
        self.texture = json_file["id"][self.id].get("texture")
        self.hitbox = json_file["id"][self.id].get("hitbox")
        self.name = json_file["id"][self.id].get("name")
        self.description = json_file["id"][self.id].get("description")
        self.strength = json_file["id"][self.id].get("strength")
        self.use = json_file["id"][self.id].get("use")

        if self.use == True:
            self.result_use = json_file["id"][self.id].get("result_use")

        drop_num = self.drop.count(0)
        if drop_num >= 2:
            for i in reversed(range(len(self.drop))):
                if drop_num == 1:
                    break
                if self.drop[i] == 0:
                    self.drop.pop(i)
                    drop_num -= 1

        if self.idc != self.id:
            self.drop = json_file["id"][self.id].get("drop")
        self.idc = self.id

    def generation(self):
        self.id = random.randint(0, 2)