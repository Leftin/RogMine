import msvcrt
import json
import random
from os import system
import DATA.items.items as item
import DATA.hero.craft as craft
import DATA.map.map

class hero():
    def __init__(self, slots):
        self.mode = 2
        self.texture = "☺"
        self.worldx = 5
        self.worldy = 5
        self.x = 5
        self.y = 5
        self.inventory = list()
        self.slots = slots
        self.id_near = [0, 0, 0, 0, 0, 0, 0, 0]
        self.strength = 0
        for i in range(self.slots):
            self.inventory.append(item.item())
        
    
    def control(self, map, world):

        xc = self.x
        yc = self.y

        var = msvcrt.getch()
        if ord(var) == ord("8"):
            yc -= 1
        if ord(var) == ord("2"):
            yc += 1
        if ord(var) == ord("4"):
            xc -= 1
        if ord(var) == ord("6"):
            xc += 1
        
        if ord(var) == ord("m"):
            self.mine(map)
        if ord(var) == ord("i"):
            self.print_inv(world)
        if ord(var) == ord("x"):
            self.inspection(map)
        if ord(var) == ord("c"):
            craft.craft(self, map)
        if ord(var) == ord("b"):
            self.build(map)
        if ord(var) == ord("u"):
            self.use(map, world)
        if ord(var) == ord("t"):
            self.take(map)
        if ord(var) == ord("d"):
            self.drop(map)
        if ord(var) == ord("h"):
            self.help()
        if ord(var) == ord("s"):
            self.save(world)
        if ord(var) == ord("l"):
            self.load(world)
        if ord(var) == ord("w"):
            self.world_move(world)
        if ord(var) == 27: # Esc
            self.pause(map)
        if self.mode == 2:
            if ord(var) == ord("g"):
                self.give()

        if xc > map.x-1:
            xc = self.x
        if xc < 0:
            xc = self.x
        if yc > map.y-1:
            yc = self.y
        if yc < 0:
            yc = self.y

        if map.board[yc][xc].hitbox == True:
                xc = self.x
                yc = self.y

        self.x = xc
        self.y = yc
    
    def get_resourse(self, resourse: list):
        for i in range(len(resourse)):
            for j in range(len(self.inventory)):
                if self.inventory[j].id == 0:
                    self.inventory[j].id = resourse[i]
                    break

    def update_inv(self):
        self.cout_null_item = 0
        for i in range(len(self.inventory)):
            self.inventory[i].update()
            if self.inventory[i].id == 0:
                self.cout_null_item += 1

        i=0
        j = 0
        for i in range(len(self.inventory)):
            if self.inventory[i].strength > j:
                j = self.inventory[i].strength

        self.strength = j
    def print_inv(self, world):
        run = True
        j = 0
        while run:
            system("cls")
            print("══════")
            for i in range(len(self.inventory)):
                if i == j:
                    print(f"{i+1}. {self.inventory[i].name} <--")
                else:
                    print(f"{i+1}. {self.inventory[i].name}")
            print("══════")
            print(f"Strength: {self.inventory[j].strength}")
            print(f"Build: {self.inventory[j].build}")
            if self.inventory[j].id == 15:
                print(f"Time: {world.clock}")

            var = msvcrt.getch()
            if ord(var) == ord("2"):
                j += 1
            if ord(var) == ord("8"):
                j -= 1
            if ord(var) == ord("x"):
                run = False

    def update_idnear(self, map):
        self.id_near = list()
        if self.x < map.x-1:
            self.id_near.append(map.board[self.y][self.x+1].id)
            if self.y > 0:
                self.id_near.append(map.board[self.y-1][self.x+1].id)
            if self.y < map.y-1:
                self.id_near.append(map.board[self.y+1][self.x+1].id)
        if self.x > 0:
            self.id_near.append(map.board[self.y][self.x-1].id)
            if self.y > 0:
                self.id_near.append(map.board[self.y-1][self.x-1].id)
            if self.y < map.y-1:
                self.id_near.append(map.board[self.y+1][self.x-1].id)
        if self.y > 0:
            self.id_near.append(map.board[self.y-1][self.x].id)
        if self.y < map.y-1:
            self.id_near.append(map.board[self.y+1][self.x].id)

    def build(self, map: object):
            xc = self.x
            yc = self.y
            print("Where do you want to put the cell?")
            var = msvcrt.getch()
            if ord(var) == ord("8"):
                yc -= 1
            if ord(var) == ord("2"):
                yc += 1
            if ord(var) == ord("4"):
                xc -= 1
            if ord(var) == ord("6"):
                xc += 1
            
            if map.board[yc][xc].id == 0:
                run = True
                j = 0
                while run:
                    system("cls")
                    if j < 0:
                        j = 0
                    elif j > len(self.inventory):
                        j = len(self.inventory)
                    print("══════")
                    for i in range(len(self.inventory)):
                        if i == j:
                            print(f"{i+1}. {self.inventory[i].name} <--")
                        else:
                            print(f"{i+1}. {self.inventory[i].name}")
                    print("══════")
                    print("\n2 - next\n8 - back\n5 - ready\n\nx - cancel")
                    var = msvcrt.getch()
                    if ord(var) == ord("2"):
                        j += 1
                    if ord(var) == ord("8"):
                        j -= 1
                    elif ord(var) == ord("x"):
                        run = False
                    if ord(var) == ord("5"):
                        if self.inventory[j].build == True:
                            if len(self.inventory[j].result_build) == 1:
                                map.board[yc][xc].id = self.inventory[j].result_build[0]
                                self.inventory[j].id = 0
                                run = False
                            else:
                                run2 = True
                                k = 0
                                f = open("DATA\map\cell.json", "r")
                                json_file = json.load(f)
                                while run2:
                                    system("cls")
                                    print("What do you want to put?")
                                    for i in range(len(self.inventory[j].result_build)):
                                        print(json_file["id"][self.inventory[j].result_build[i]].get("name"), end="")
                                        if i==k:
                                            print("<--", end="")
                                        print()
                                    print("\n2 - next\n8 - back\n5 - ready\n\nx - cancel")
                                    var = msvcrt.getch()
                                    if ord(var) == ord("2"):
                                        k += 1
                                    if ord(var) == ord("8"):
                                        k -= 1
                                    if ord(var) == ord("x"):
                                        run2=False
                                    if ord(var) == ord("5"):
                                        build = self.inventory[j].result_build[k]
                                        map.board[yc][xc].id = build
                                        self.inventory[j].id = 0
                                        run2=False
                                        run=False

            else:
                map.alert = "The place is busy!"
    def use(self, map: object, world: object):

            xc = self.x
            yc = self.y
            print("what do you want to use?")
            var = msvcrt.getch()
            if ord(var) == ord("8"):
                yc -= 1
            if ord(var) == ord("2"):
                yc += 1
            if ord(var) == ord("4"):
                xc -= 1
            if ord(var) == ord("6"):
                xc += 1
            if hasattr(map.board[yc][xc], "result_use"):
                map.board[yc][xc].id = map.board[yc][xc].result_use
                if map.board[yc][xc].id == 10:
                    blocks = [2, 8, 9, 11]
                    if world.clock-map.board[yc][xc].clock >= 5:
                        if self.cout_null_item <= 0:
                            map.alert = "Not enough space"
                        else:
                            self.get_resourse([random.choice(blocks)])
                            map.board[yc][xc].clock = world.clock
                    else:
                        map.alert = "The time has not come"

            else:
                self.alert = "This cell cannot be used"
    def inspection(self, map: object):
            xc = self.x
            yc = self.y
            run = True
            while run:
                system("cls")   
                map.board[self.y][self.x].texture = self.texture
                map.board[yc][xc].texture = "x"

                map.write()
                print(f"Name: {map.board[yc][xc].name}")
                print(f"Description: {map.board[yc][xc].description}")
                print(f"Id: {map.board[yc][xc].id}")
                print(f"Hitbox: {map.board[yc][xc].hitbox}")
                print(f"Need strength: {map.board[yc][xc].need_strength}")
                print(f"Drop: {map.board[yc][xc].drop}")
                if xc == self.x and yc == self.y:
                    print("\nThis is you")
                print("\nx - cancel")
                var = msvcrt.getch()

                f = open("DATA\map\cell.json")
                json_file = json.load(f)                
                map.board[yc][xc].texture = json_file["id"][map.board[yc][xc].id].get("texture")

                if ord(var) == ord("8"):
                    yc -= 1
                if ord(var) == ord("2"):
                    yc += 1
                if ord(var) == ord("4"):
                    xc -= 1
                if ord(var) == ord("6"):
                    xc += 1
                
                if xc > map.x-1:
                    xc -= 1
                if xc < 0:
                    xc += 1
                if yc > map.y-1:
                    yc -= 1
                if yc < 0:
                    yc += 1

                if ord(var) == ord("x"):
                    run = False
                    xc = self.x
                    yc = self.y
                
                if self.mode == 2:
                    if ord(var) == ord("5"):
                        f = open("DATA\map\cell.json", "r")
                        json_file = json.load(f)
                        blocks = json_file["id"]
                        j = 0
                        run2 = True
                        while run2:
                            system("cls")
                            for i in range(len(blocks)):
                                print(blocks[i]["name"], end="")
                                if i == j:
                                    print("<--", end="")
                                print()
                            print("\n2 - next\n8 - back\n5 - ready\n\nx - cancel")
                            var = msvcrt.getch()
                            if ord(var) == ord("2"):
                                j += 1
                            elif ord(var) == ord("8"):
                                j -= 1
                            elif ord(var) == ord("x"):
                                run2 = False    
                            elif ord(var) == ord("5"):
                                 map.board[yc][xc].id = j
                                 run2 = False


    def mine(self, map: object):
            xc = self.x
            yc = self.y
            print("What block do you want to mine?")
            var = msvcrt.getch()
            if ord(var) == ord("8"):
                yc -= 1
            if ord(var) == ord("2"):
                yc += 1
            if ord(var) == ord("4"):
                xc -= 1
            if ord(var) == ord("6"):
                xc += 1
            if self.mode == 1:
                if map.board[yc][xc].mine != False:
                        if map.board[yc][xc].need_strength <= self.strength:
                            if self.cout_null_item >= len(map.board[yc][xc].drop):
                                map.board[yc][xc].id = 0
                                self.get_resourse(map.board[yc][xc].drop)
                            else:
                                map.alert = "Not enough space"
                        else:
                            map.alert = "Need a more powerful tool"
                else:
                    map.alert = "This cell cannot be mined"
            else:
                map.board[yc][xc].id = 0
    def take(self, map: object):
            xc = self.x
            yc = self.y
            print("On which cell do you want to take the item?")
            var = msvcrt.getch()
            if ord(var) == ord("8"):
                yc -= 1
            if ord(var) == ord("2"):
                yc += 1
            if ord(var) == ord("4"):
                xc -= 1
            if ord(var) == ord("6"):
                xc += 1        

            j=0
            if map.board[yc][xc].hitbox == False:
                run = True
                f = open("DATA\items\items.json", "r")
                json_file = json.load(f)
                while run:
                    system("cls")
                    print("══════")
                    for i in range(len(map.board[yc][xc].drop)):
                        if i == j:
                            print(str(i+1) + "." + json_file["id"][map.board[yc][xc].drop[i]].get("name") + "<--")
                        else:
                            print(str(i+1) + "." + json_file["id"][map.board[yc][xc].drop[i]].get("name"))
                    print("══════")
                    print("\n2 - next\n8 - back\n5 - ready\n\nx - cancel")
                    var = msvcrt.getch()
                    if ord(var) == ord("2"):
                        j += 1
                    elif ord(var) == ord("8"):
                        j -= 1
                    elif ord(var) == ord("x"):
                        run = False    
                    elif ord(var) == ord("5"):
                        self.get_resourse([map.board[yc][xc].drop[j]])
                        map.board[yc][xc].drop[j] = 0
                        break
    def drop(self, map: object):
        xc = self.x
        yc = self.y
        print("On which cell do you want to take the item?")
        var = msvcrt.getch()
        if ord(var) == ord("8"):
            yc -= 1
        if ord(var) == ord("2"):
            yc += 1
        if ord(var) == ord("4"):
            xc -= 1
        if ord(var) == ord("6"):
            xc += 1  
        j = 0    
        run = True
        while run:
            system("cls")
            for i in range(len(self.inventory)):
                if i == j:
                    print(f"{i+1}. {self.inventory[i].name} <--")
                else:
                    print(f"{i+1}. {self.inventory[i].name}")
            print("\n2 - next\n8 - back\n5 - ready\n\nx - cancel")
            var = msvcrt.getch()
            if ord(var) == ord("2"):
                j += 1
            elif ord(var) == ord("8"):
                j -= 1
            elif ord(var) == ord("x"):
                run = False
            elif ord(var) == ord("5"):
                map.board[yc][xc].drop.append(self.inventory[j].id)
                self.inventory[j].id = 0
                break
    def help(self):
        system("cls")
        print("2, 4, 8, 6 - move")
        print("m - mine")
        print("b - build")
        print("c - craft")
        print("u - use")
        print("x - inspection")
        print("d - drop")
        print("t - take")
        print("s - save map")
        print("l - load map")
        print("w - go around the world")
        msvcrt.getch()
    def save(self, world: object):
        world.save()
        f = open(f"DATA\saves\\{world.name}\hero.json", "w")
        inventory_id = list()
        for i in range(len(self.inventory)):
            inventory_id.append(self.inventory[i].id)
        json.dump(inventory_id, f)
    def load(self, world: object):
        world.load()
        f = open(f"DATA\saves\\{world.name}\hero.json", "r")
        load_inventory = json.load(f)
        for i in range(len(self.inventory)):
            self.inventory[i].id = load_inventory[i]
    def pause(self, map: object):
        map.pause()
    def world_move(self, world: object):
        run = True
        while run:
            system("cls")
            world.board[self.worldy][self.worldx].texture = "☺"
            world.write()
            world.board[self.worldy][self.worldx].update_texture()
            var = msvcrt.getch()
            if ord(var) == ord("8"):
                self.worldy -= 1
            if ord(var) == ord("2"):
                self.worldy += 1
            if ord(var) == ord("4"):
                self.worldx -= 1
            if ord(var) == ord("6"):
                self.worldx += 1
            if ord(var) == ord("x"):
                run = False
    def give(self):
        f = open("DATA\items\items.json", "r")
        json_file = json.load(f)
        items = json_file["id"]
        j = [0]
        run = True
        give = False
        while run:
            system("cls")
            for i in range(len(items)):
                print(items[i]["name"], end="")
                if i == j[0]:
                    print("<--", end="")
                print()
            print("\n2 - next\n8 - back\n5 - ready\n\nx - cancel")
            if give == True: print("Item give")
            var = msvcrt.getch()
            if give == True: give = False
            if ord(var) == ord("2"):
                j[0] += 1
            elif ord(var) == ord("8"):
                j[0] -= 1
            elif ord(var) == ord("x"):
                run = False
            elif ord(var) == ord("5"):
                self.get_resourse(j)
                give = True