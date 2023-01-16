import DATA.map.cell
import random

class map():
    def __init__(self, mapX, mapY):
        self.x = mapX
        self.y = mapY
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

    def update(self):
        for i in range(self.y):
            for j in range(self.x):
                self.board[i][j].update()
    
    def generation(self):
        for i in range(self.y):
            for j in range(self.x):
                self.board[i][j].id = random.randint(0, 2)