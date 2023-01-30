# overworld
# Osi's The Wastes

import UI
import loaders
import copy
import random

import world
import city
import convoy
import vehicle
import weapon
import upgrade
import cargo

def move(world, playerConvoy):
    moved = 0
    UI.printWorld(world, playerConvoy)
    UI.printTextBox(str(playerConvoy.fuel) + " fuel remaining")
    UI.printTextBox("WASD to move, i to check vehicles and inventory")
    tmpMoveDirection = input()
    if tmpMoveDirection == "":
        tmpMoveDirection = "-1"
    moveDirection = tmpMoveDirection
    
    if moveDirection == "w" and (0 <= playerConvoy.y - 1) and (5 != world.terrain[playerConvoy.x][playerConvoy.y - 1]):
        playerConvoy.y = playerConvoy.y - 1
        moved = 1
    elif moveDirection == "s" and (playerConvoy.y + 1 < 30) and (5 != world.terrain[playerConvoy.x][playerConvoy.y + 1]):
        playerConvoy.y = playerConvoy.y + 1
        moved = 1
    elif moveDirection == "a" and (0 <= playerConvoy.x - 1) and (5 != world.terrain[playerConvoy.x - 1][playerConvoy.y]):
        playerConvoy.x = playerConvoy.x - 1
        moved = 1
    elif moveDirection == "d" and (playerConvoy.x + 1 < 50) and (5 != world.terrain[playerConvoy.x + 1][playerConvoy.y]):
        playerConvoy.x = playerConvoy.x + 1
        moved = 1
    elif moveDirection == "i":
        UI.printTextBox("Inventory:")
        UI.printConvoy(playerConvoy)
        UI.printTextBox("Press [enter] to continue")
        nuthin = input()
    
    print("\n" * 4)

    if moved == 1:
        if world.terrain[playerConvoy.x][playerConvoy.y] <= 10:
            playerConvoy.fuel = playerConvoy.fuel - (playerConvoy.size * (world.terrain[playerConvoy.x][playerConvoy.y] + 1))
    else:
        UI.printTextBox("Invalid movement")   

def overworld(world, playerConvoy, shopVehicles, enemyVehicles, weapons, upgrades):
    while True:
        if playerConvoy.fuel <= 0:
            UI.printTextBox("You ran out of fuel, numbnuts.")
            print("\n")
            UI.printTextBox("GAME OVER awwwww...")
            break

        if world.cityName[playerConvoy.x][playerConvoy.y] != "":
            city.city(world, playerConvoy, shopVehicles, weapons, upgrades)

        if playerConvoy.x == 4 and playerConvoy.y == 20:
            UI.printTextBox("You made it to LA!")
            UI.printTextBox("However, upon arrival, you realize")
            UI.printTextBox("it's LA.")
            UI.printTextBox("Time to head back!")
            print("\n")
            UI.printTextBox("GAME OVER YEAAAAAAAAAAH!!!")
            UI.printTextBox("Press [enter] to close the game")
            nuthin = input()
            break

        move(world, playerConvoy)