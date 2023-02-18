# import files
import DATA.map.cell
import DATA.items.items
import DATA.map.world as m
import DATA.hero.hero as h

"""
RogMine Version 0.3 (build 6)
"""
# import modules
import json
import msvcrt
import os
import random

# game values
mapX = 15
mapY = 10
worldX = 10
worldY = 10
slots_inventory = 5

print("Generate world...") # alert generation

hero = h.hero(slots_inventory) # init hero
world = m.world(worldX, worldY, mapX, mapY) # init map
map = world.board[hero.worldy][hero.worldx] # init map
world.generation()

os.system("cls") # clear screen

hero.get_resourse([2, 2, 2, 8]) # get start resourses hero

map.alert = "Press h to help" # start alert

while True: # main loop
    map = world.board[hero.worldy][hero.worldx]
    map.update() # update map
    hero.update_inv() # update hero inventory
    hero.update_idnear(map) # update id near hero
    map.board[hero.y][hero.x].texture = hero.texture # set player texture
    os.system("cls") # clear screen
    map.write() # write map
    map.clock += 1 # clock +
    hero.control(map, world) # control