import msvcrt
import json
from os import system
import DATA.items.items as item
import DATA.items.craft as craft

class hero():
    def __init__(self):
        self.texture = "☺"
        self.x = 5
        self.y = 5
        self.inventory = list()
        self.slots = 5
        self.strength = 1
        for i in range(self.slots):
            self.inventory.append(item.item())
    
    def control(self, map):

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
            
            if map.board[yc][xc].strength <= self.strength:
                map.board[yc][xc].id = 0
                self.get_resourse(map.board[yc][xc].drop)
        if ord(var) == ord("i"):
            self.print_inv()
        if ord(var) == ord("x"):
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
                print(f"Strength: {map.board[yc][xc].strength}")
                print(f"Drop: {map.board[yc][xc].drop}")
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
                
                if ord(var) == ord("x"):
                    run = False
                    xc = self.x
                    yc = self.y
        if ord(var) == ord("c"):
            craft.craft(self)
        if ord(var) == ord("b"):
            self.build(map)
        if ord(var) == ord("u"):
            self.use(map)
            
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
        for i in range(len(self.inventory)):
            self.inventory[i].update()

        i=0
        j = 0
        for i in range(len(self.inventory)):
            if self.inventory[i].strength > j:
                j = self.inventory[i].strength
        
        self.strength = j

    
    def print_inv(self):
        run = True
        j = 0
        while run:
            system("cls")
            for i in range(len(self.inventory)):
                if i == j:
                    print(f"{i+1}. {self.inventory[i].name} <--")
                else:
                    print(f"{i+1}. {self.inventory[i].name}")

            print(f"Strength: {self.inventory[j].strength}")
            print(f"Build: {self.inventory[j].build}")

            var = msvcrt.getch()
            if ord(var) == ord("2"):
                j += 1
            if ord(var) == ord("8"):
                j -= 1
            if ord(var) == ord("x"):
                run = False
    
    def build(self, map):
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
                    for i in range(len(self.inventory)):
                        if i == j:
                            print(f"{i+1}. {self.inventory[i].name} <--")
                        else:
                            print(f"{i+1}. {self.inventory[i].name}")
                    var = msvcrt.getch()
                    if ord(var) == ord("2"):
                        j += 1
                    if ord(var) == ord("8"):
                        j -= 1
                    if ord(var) == ord("5"):
                        if self.inventory[j].build == True:
                            map.board[yc][xc].id = self.inventory[j].result
                            self.inventory[j].id = 0
                            run = False
            else:
                print("The place is busy!")
                msvcrt.getch()
    
    def use(self, map):
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
            if map.board[yc][xc].use == True:
                map.board[yc][xc].id = map.board[yc][xc].result_use
            else:
                print("This cell cannot be used")
                msvcrt.getch()