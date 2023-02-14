# import files
import DATA.map.cell
import DATA.items.items
import DATA.map.map as m
import DATA.hero.hero as h

"""
RogMine Version 0.2 (build 4)
v0.1
Craft
Drop/take item
Generate map
v0.2
Save\load map
New generate map
"""
# import modules
import json
import msvcrt
import os
import random

# game values
mapX = 10
mapY = 10
slots_inventory = 5

hero = h.hero(slots_inventory) # init hero
map = m.map(mapX, mapY) # init map

map.generation() # generation map
hero.get_resourse([]) # get resourses hero


while True: # main loop
    map.update() # update map
    hero.update_inv() # update hero inventory
    map.board[hero.y][hero.x].texture = hero.texture # set player texture
    os.system("cls") # clear screen
    map.write() # write map
    hero.control(map) # control