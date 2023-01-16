import DATA.map.cell
import DATA.items.items
import DATA.map.map as m
import DATA.hero.hero as h

"""
RogMine Version 0.1 (build 3)
"""

import msvcrt
import os
import random

mapX = 10
mapY = 10

hero = h.hero()
map = m.map(mapX, mapY)

map.generation()
hero.get_resourse([2, 2])

while True: # main loop
    map.update() # update map
    hero.update_inv() # update hero inventory
    map.board[hero.y][hero.x].texture = hero.texture # set player texture
    os.system("cls") # clear screen
    map.write() # write map
    hero.control(map) # control