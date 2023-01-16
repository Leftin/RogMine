import json
import random

class cell():
    def __init__(self):
        self.id = 0
    
    def update(self):
        f = open("DATA\map\cell.json")
        json_file = json.load(f)
        
        self.texture = json_file["id"][self.id].get("texture")
        self.hitbox = json_file["id"][self.id].get("hitbox")
        self.name = json_file["id"][self.id].get("name")
        self.description = json_file["id"][self.id].get("description")
        self.strength = json_file["id"][self.id].get("strength")
        self.use = json_file["id"][self.id].get("use")
        self.drop = json_file["id"][self.id].get("drop")

        if self.use == True:
            self.result_use = json_file["id"][self.id].get("result_use")
    
    def generation(self):
        self.id = random.randint(0, 2)