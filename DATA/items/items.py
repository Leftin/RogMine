import json

class item():
    def __init__(self):
        self.id = 0
    
    def update(self):
        f = open("DATA\items\items.json")
        json_file = json.load(f)
        
        self.name = json_file["id"][self.id].get("name")
        self.strength = json_file["id"][self.id].get("strength")
        self.build = json_file["id"][self.id].get("build")
        if self.build == True:
            self.result_build = json_file["id"][self.id].get("result_build")