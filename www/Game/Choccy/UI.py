# UI
# Osi's The Wastes

import convoy
import vehicle
import weapon
import time
import random

printSpeed = 0.0005 # how long it takes to print each character (in seconds)
boxWidth = 96 # must be divisible by 2 and 3
if boxWidth % 2 != 0 or boxWidth % 3 != 0:
    print("*****************" * 4)
    print("INVALID BOX WIDTH")
    print("*****************" * 4)

def inputNumber():
    tmpChoice = input()
    if tmpChoice != "": # if type =/= number, throw it out
        tmpChoice = "-1"
    choice = int(tmpChoice)

def print_slowly(text, **kwargs):
    for character in text:
        print(character, end = "", flush = True)
        time.sleep(random.random() * printSpeed)
    if "end" in kwargs:
        pass
    else:
        print(flush = True)

def printTextBox(text):
    if text == "":
        text = " "

    print_slowly("╔", end = "")
    for i in range(boxWidth + 4): print_slowly("═", end = "")
    print_slowly("╗")

    lines = 1
    if len(text) > boxWidth:
        lines = int(len(text) / boxWidth) + 1
    for i in range(boxWidth):
        text = text + " "
    
    for lineIndex in range(lines):
        print_slowly("║ ", end = "")
        print_slowly(text[lineIndex * (boxWidth + 2) : (lineIndex + 1) * (boxWidth + 2)], end = "")
        for i in range(boxWidth - len(text[lineIndex * (boxWidth + 2) : (lineIndex + 1) * (boxWidth + 2)]) + 2): print_slowly(" ", end = "")
        
        if text[((lineIndex + 1) * (boxWidth + 2)) - 1] == " " or text[(lineIndex + 1) * (boxWidth + 2)] == " ":
            print_slowly(" ", end = "")
        else:
            print_slowly("-", end = "")
        print_slowly("║")

    print_slowly("╚", end = "")
    for i in range(boxWidth + 4): print_slowly("═", end = "")
    print_slowly("╝")

def printQuadMenu(options):
    print_slowly("╔", end = "")
    for i in range(int(boxWidth / 2)): print_slowly("═", end = "")
    print_slowly("╤", end = "")
    for i in range(int(boxWidth / 2)): print_slowly("═", end = "")
    print_slowly("╗")

    print_slowly("║    ", end = "") if options[0] == "" else print_slowly("║ 1. " + options[0], end = "")
    for i in range(int(boxWidth / 2)  - len(options[0]) - 4): print_slowly(" ", end = "")
    print_slowly("│    ", end = "") if options[1] == "" else print_slowly("│ 2. " + options[1], end = "")
    for i in range(int(boxWidth / 2)  - len(options[1]) - 4): print_slowly(" ", end = "")
    print_slowly("║")

    print_slowly("╟", end = "")
    for i in range(int(boxWidth / 2)): print_slowly("─", end = "")
    print_slowly("┼", end = "")
    for i in range(int(boxWidth / 2)): print_slowly("─", end = "")
    print_slowly("╢")

    print_slowly("║    ", end = "") if options[2] == "" else print_slowly("║ 3. " + options[2], end = "")
    for i in range(int(boxWidth / 2)  - len(options[2]) - 4): print_slowly(" ", end = "")
    print_slowly("│    ", end = "") if options[3] == "" else print_slowly("│ 4. " + options[3], end = "")
    for i in range(int(boxWidth / 2)  - len(options[3]) - 4): print_slowly(" ", end = "")
    print_slowly("║")

    print_slowly("╚", end = "")
    for i in range(int(boxWidth / 2)): print_slowly("═", end = "")
    print_slowly("╧", end = "")
    for i in range(int(boxWidth / 2)): print_slowly("═", end = "")
    print_slowly("╝")

def printHexMenu(options):
    print_slowly("╔", end = "")
    for i in range(int(boxWidth / 3)): print_slowly("═", end = "")
    print_slowly("╤", end = "")
    for i in range(int(boxWidth / 3)): print_slowly("═", end = "")
    print_slowly("╤", end = "")
    for i in range(int(boxWidth / 3)): print_slowly("═", end = "")
    print_slowly("╗")

    print_slowly("║    ", end = "") if options[0] == "" else print_slowly("║ 1. " + options[0], end = "")
    for i in range(int(boxWidth / 3)  - len(options[0]) - 4): print_slowly(" ", end = "")
    print_slowly("│    ", end = "") if options[1] == "" else print_slowly("│ 2. " + options[1], end = "")
    for i in range(int(boxWidth / 3)  - len(options[1]) - 4): print_slowly(" ", end = "")
    print_slowly("│    ", end = "") if options[2] == "" else print_slowly("│ 3. " + options[2], end = "")
    for i in range(int(boxWidth / 3)  - len(options[2]) - 4): print_slowly(" ", end = "")
    print_slowly("║")

    print_slowly("╟", end = "")
    for i in range(int(boxWidth / 3)): print_slowly("─", end = "")
    print_slowly("┼", end = "")
    for i in range(int(boxWidth / 3)): print_slowly("─", end = "")
    print_slowly("┼", end = "")
    for i in range(int(boxWidth / 3)): print_slowly("─", end = "")
    print_slowly("╢")

    print_slowly("║    ", end = "") if options[3] == "" else print_slowly("║ 4. " + options[3], end = "")
    for i in range(int(boxWidth / 3)  - len(options[3]) - 4): print_slowly(" ", end = "")
    print_slowly("│    ", end = "") if options[4] == "" else print_slowly("│ 5. " + options[4], end = "")
    for i in range(int(boxWidth / 3)  - len(options[4]) - 4): print_slowly(" ", end = "")
    print_slowly("│    ", end = "") if options[5] == "" else print_slowly("│ 6. " + options[5], end = "")
    for i in range(int(boxWidth / 3)  - len(options[5]) - 4): print_slowly(" ", end = "")
    print_slowly("║")

    print_slowly("╚", end = "")
    for i in range(int(boxWidth / 3)): print_slowly("═", end = "")
    print_slowly("╧", end = "")
    for i in range(int(boxWidth / 3)): print_slowly("═", end = "")
    print_slowly("╧", end = "")
    for i in range(int(boxWidth / 3)): print_slowly("═", end = "")
    print_slowly("╝")

def printWeapons(vehicle):
    tmp = ""
    for i in range(int((boxWidth / 3) + 1)): print_slowly(" ", end = "")
    print_slowly("╒", end = "")
    for i in range(int((boxWidth / 3) + 0)): print_slowly("═", end = "")
    print_slowly("╕")

    for i in range(int((boxWidth / 3) + 1)): print_slowly(" ", end = "")
    print_slowly("│ 1. ", end = "")
    tmp = vehicle.upWeapon.name
    if vehicle.upWeapon.name != "":
        tmp = tmp + " - " + str(vehicle.upWeapon.damage) + " DMG"
    print_slowly(tmp, end = "")
    for i in range(int((boxWidth / 3)  - len(tmp) - 4)): print_slowly(" ", end = "")
    print_slowly("│")

    print_slowly("╓", end = "")
    for i in range(int((boxWidth / 3) + 0)): print_slowly("─", end = "")
    print_slowly("┼", end = "")
    for i in range(int((boxWidth / 3) + 0)): print_slowly("─", end = "")
    print_slowly("┼", end = "")
    for i in range(int((boxWidth / 3) + 0)): print_slowly("─", end = "")
    print_slowly("╖")

    print_slowly("║ 3. ", end = "")
    tmp = vehicle.leftWeapon.name
    if vehicle.leftWeapon.name != "":
        tmp = tmp + " - " + str(vehicle.leftWeapon.damage) + " DMG"
    print_slowly(tmp, end = "")
    for i in range(int((boxWidth / 3)  - len(tmp) - 4)): print_slowly(" ", end = "")
    print_slowly("│ ", end = "")
    print_slowly(vehicle.name, end = "")
    for i in range(int((boxWidth / 3)  - len(vehicle.name) - 1)): print_slowly(" ", end = "")
    print_slowly("│ 4. ", end = "")
    tmp = vehicle.rightWeapon.name
    if vehicle.rightWeapon.name != "":
        tmp = tmp + " - " + str(vehicle.rightWeapon.damage) + " DMG"
    print_slowly(tmp, end = "")
    for i in range(int((boxWidth / 3)  - len(tmp) - 4)): print_slowly(" ", end = "")
    print_slowly("║")

    print_slowly("╙", end = "")
    for i in range(int((boxWidth / 3) + 0)): print_slowly("─", end = "")
    print_slowly("┼", end = "")
    for i in range(int((boxWidth / 3) + 0)): print_slowly("─", end = "")
    print_slowly("┼", end = "")
    for i in range(int((boxWidth / 3) + 0)): print_slowly("─", end = "")
    print_slowly("╜")

    for i in range(int((boxWidth / 3) + 1)): print_slowly(" ", end = "")
    print_slowly("│ 2. ", end = "")
    tmp = vehicle.downWeapon.name
    if vehicle.downWeapon.name != "":
        tmp = tmp + " - " + str(vehicle.downWeapon.damage) + " DMG"
    print_slowly(tmp, end = "")
    for i in range(int((boxWidth / 3)  - len(tmp) - 4)): print_slowly(" ", end = "")
    print_slowly("│")

    for i in range(int((boxWidth / 3) + 1)): print_slowly(" ", end = "")
    print_slowly("╘", end = "")
    for i in range(int((boxWidth / 3) + 0)): print_slowly("═", end = "")
    print_slowly("╛")

def populateUpgradeTile(upgrades):
    empty = " " * int(boxWidth / 4)
    tiles = [[empty for i in range(4)] for line in range(6)]
    for i in range(4):
            tiles[0][i] = " " + str(i + 1) + ". " + upgrades[i].name
            upgradeIndex = 0
            if upgrades[i].AP != 0:
                if upgrades[i].AP > 0:
                    tiles[1 + upgradeIndex][i] = " +" + str(upgrades[i].AP) + " armor"
                else:
                    tiles[1 + upgradeIndex][i] = " " + str(upgrades[i].AP) + " armor"
                upgradeIndex = upgradeIndex + 1
            if upgrades[i].acceleration != 0:
                if upgrades[i].acceleration > 0:
                    tiles[1 + upgradeIndex][i] = " +" + str(upgrades[i].acceleration) + " acceleration"
                else:
                    tiles[1 + upgradeIndex][i] = " " + str(upgrades[i].acceleration) + " acceleration"
                upgradeIndex = upgradeIndex + 1
            if upgrades[i].handling != 0:
                if upgrades[i].handling > 0:
                    tiles[1 + upgradeIndex][i] = " +" + str(upgrades[i].handling) + " handling"
                else:
                    tiles[1 + upgradeIndex][i] = " " + str(upgrades[i].handling) + " handling"
                upgradeIndex = upgradeIndex + 1
            if upgrades[i].braking != 0:
                if upgrades[i].braking > 0:
                    tiles[1 + upgradeIndex][i] = " +" + str(upgrades[i].braking) + " braking"
                else:
                    tiles[1 + upgradeIndex][i] = " " + str(upgrades[i].braking) + " braking"
                upgradeIndex = upgradeIndex + 1
            if upgrades[i].capability != 0:
                if upgrades[i].capability > 0:
                    tiles[1 + upgradeIndex][i] = " +" + str(upgrades[i].capability) + " capability"
                else:
                    tiles[1 + upgradeIndex][i] = " " + str(upgrades[i].capability) + " capability"
                upgradeIndex = upgradeIndex + 1
            
            description = upgrades[i].description
            tiles[4][i] = " " + description[: int(boxWidth / 4) - 2]
            tiles[5][i] = " " + description[int(boxWidth / 4) - 2 :]
            if len(description) > int(boxWidth / 4):
                if description[int(boxWidth / 4) - 2 - 1] != " " and description[int(boxWidth / 4) - 2] != " ":
                    tiles[4][i] = tiles[4][i] + "-"
    return tiles

def printUpgrades(vehicle):
    tiles = populateUpgradeTile(vehicle.upgrades)

    print_slowly("╔", end = "")
    for j in range(4):
        for k in range(int(boxWidth / 4)): print_slowly("═", end = "")
        if j != 3:
            print_slowly("╤", end = "")
        else:
            print_slowly("╗")

    for line in range(6):
        print_slowly("║", end = "")
        for i in range(4):
            print_slowly(tiles[line][i], end = "")
            for k in range(int(boxWidth / 4)  - len(tiles[line][i])): print_slowly(" ", end = "")
            if i != 3:
                print_slowly("│", end = "")
            else:
                print_slowly("║")

    print_slowly("╚", end = "")
    for j in range(4):
        for k in range(int(boxWidth / 4)): print_slowly("═", end = "")
        if j != 3:
            print_slowly("╧", end = "")
        else:
            print_slowly("╝")

def populateCargoTiles(cargo):
    empty = " " * int(boxWidth / 4)
    tiles = [[[empty for y in range(4)] for x in range(4)] for line in range(6)]
    for y in range(4):
        for x in range(4):

            if cargo[(y * 4) + x].content == "package":
                tiles[0][x][y] = " " + str((y * 4) + x + 1) + ". " + cargo[(y * 4) + x].name
                tiles[1][x][y] = " Destination:"
                tiles[2][x][y] = " " + str(cargo[(y * 4) + x].destination)
                tiles[3][x][y] = " $" + str(cargo[(y * 4) + x].awardForDelivery) + " upon delivery"
                description = cargo[(y * 4) + x].description.strip()

            elif cargo[(y * 4) + x].content == "weapon":
                tiles[0][x][y] = " " + str((y * 4) + x + 1) + ". " + cargo[(y * 4) + x].cargoWeapon.name
                tiles[2][x][y] = " " + str(cargo[(y * 4) + x].cargoWeapon.damage) + " - DMG"
                description = cargo[(y * 4) + x].cargoWeapon.description.strip()
                
            elif cargo[(y * 4) + x].content == "upgrade":
                tiles[0][x][y] = " " + str((y * 4) + x + 1) + ". " + cargo[(y * 4) + x].cargoUpgrade.name
                upgradeIndex = 0
                if cargo[(y * 4) + x].cargoUpgrade.AP != 0:
                    if cargo[(y * 4) + x].cargoUpgrade.AP > 0:
                        tiles[1 + upgradeIndex][x][y] = " +" + str(cargo[(y * 4) + x].cargoUpgrade.AP) + " armor"
                    else:
                        tiles[1 + upgradeIndex][x][y] = " " + str(cargo[(y * 4) + x].cargoUpgrade.AP) + " armor"
                    upgradeIndex = upgradeIndex + 1
                if cargo[(y * 4) + x].cargoUpgrade.acceleration != 0:
                    if cargo[(y * 4) + x].cargoUpgrade.acceleration > 0:
                        tiles[1 + upgradeIndex][x][y] = " +" + str(cargo[(y * 4) + x].cargoUpgrade.acceleration) + " acceleration"
                    else:
                        tiles[1 + upgradeIndex][x][y] = " " + str(cargo[(y * 4) + x].cargoUpgrade.acceleration) + " acceleration"
                    upgradeIndex = upgradeIndex + 1
                if cargo[(y * 4) + x].cargoUpgrade.handling != 0:
                    if cargo[(y * 4) + x].cargoUpgrade.handling > 0:
                        tiles[1 + upgradeIndex][x][y] = " +" + str(cargo[(y * 4) + x].cargoUpgrade.handling) + " handling"
                    else:
                        tiles[1 + upgradeIndex][x][y] = " " + str(cargo[(y * 4) + x].cargoUpgrade.handling) + " handling"
                    upgradeIndex = upgradeIndex + 1
                if cargo[(y * 4) + x].cargoUpgrade.braking != 0:
                    if cargo[(y * 4) + x].cargoUpgrade.braking > 0:
                        tiles[1 + upgradeIndex][x][y] = " +" + str(cargo[(y * 4) + x].cargoUpgrade.braking) + " braking"
                    else:
                        tiles[1 + upgradeIndex][x][y] = " " + str(cargo[(y * 4) + x].cargoUpgrade.braking) + " braking"
                    upgradeIndex = upgradeIndex + 1
                if cargo[(y * 4) + x].cargoUpgrade.capability != 0:
                    if cargo[(y * 4) + x].cargoUpgrade.capability > 0:
                        tiles[1 + upgradeIndex][x][y] = " +" + str(cargo[(y * 4) + x].cargoUpgrade.capability) + " capability"
                    else:
                        tiles[1 + upgradeIndex][x][y] = " " + str(cargo[(y * 4) + x].cargoUpgrade.capability) + " capability"
                    upgradeIndex = upgradeIndex + 1
                description = cargo[(y * 4) + x].cargoUpgrade.description.strip()

            else:
                description = ""

            tiles[4][x][y] = " " + description[: int(boxWidth / 4) - 2]
            tiles[5][x][y] = " " + description[int(boxWidth / 4) - 2 :]
            if len(description) > int(boxWidth / 4):
                if description[int(boxWidth / 4) - 2 - 1] != " " and description[int(boxWidth / 4) - 2] != " ":
                    tiles[4][x][y] += "-"
            if len(tiles[4][x][y]) < int(boxWidth / 4):
                tiles[4][x][y] += " " * int((boxWidth / 4) - len(tiles[4][x][y]))
            if len(tiles[5][x][y]) < int(boxWidth / 4):
                tiles[5][x][y] += " " * int((boxWidth / 4) - len(tiles[5][x][y]))
    return tiles

def printCargo(convoy):
    tiles = populateCargoTiles(convoy.cargo)

    print_slowly("╔", end = "")
    for j in range(4):
        for i in range(int(boxWidth / 4)): print_slowly("═", end = "")
        if j != 3:
            print_slowly("╤", end = "")
        else:
            print_slowly("╗")

    for y in range(4):
        for line in range(4):
            print_slowly("║", end = "")
            for x in range(4):
                print_slowly(tiles[line][x][y], end = "")
                for i in range(int(boxWidth / 4)  - len(tiles[line][x][y])): print_slowly(" ", end = "")
                if x != 3:
                    print_slowly("│", end = "")
                else:
                    print_slowly("║")

        print_slowly("║", end = "") # space for description
        for x in range(4):
            print_slowly(" " * int(boxWidth / 4), end = "")
            if x != 3:
                print_slowly("│", end = "")
            else:
                print_slowly("║")

        for line in range(4, 6):
            print_slowly("║", end = "")
            for x in range(4):
                print_slowly(tiles[line][x][y], end = "")
                for i in range(int(boxWidth / 4)  - len(tiles[line][x][y])): print_slowly(" ", end = "")
                if x != 3:
                    print_slowly("│", end = "")
                else:
                    print_slowly("║")

        if y != 3:
            print_slowly("╟", end = "")
            for j in range(4):
                for i in range(int(boxWidth / 4)): print_slowly("─", end = "")
                if j != 3:
                    print_slowly("┼", end = "")
                else:
                    print_slowly("╢")

    print_slowly("╚", end = "")
    for j in range(4):
        for i in range(int(boxWidth / 4)): print_slowly("═", end = "")
        if j != 3:
            print_slowly("╧", end = "")
        else:
            print_slowly("╝")

def populatePriceTiles(merch):
    empty = " " * int(boxWidth / 4)
    tiles = [[empty for y in range(4)] for x in range(4)]
    for y in range(4):
        for x in range(4):
            if merch[(y * 4) + x].content == "package":
                #tiles[x][y] = " $" + str(merch[(y * 4) + x].awardForDelivery)
                tiles[x][y] = " $" + str(100)

            elif merch[(y * 4) + x].content == "weapon":
                tiles[x][y] = " $" + str(merch[(y * 4) + x].cargoWeapon.value)
                
            elif merch[(y * 4) + x].content == "upgrade":
                tiles[x][y] = " $" + str(merch[(y * 4) + x].cargoUpgrade.value)
    
            if len(tiles[x][y]) < int(boxWidth / 4):
                tiles[x][y] += " " * int((boxWidth / 4) - len(tiles[x][y]))
    
    return tiles

def printMarketInv(merch):
    tiles = populateCargoTiles(merch)
    prices = populatePriceTiles(merch)
    
    print_slowly("╔", end = "")
    for j in range(4):
        for i in range(int(boxWidth / 4)): print_slowly("═", end = "")
        if j != 3:
            print_slowly("╤", end = "")
        else:
            print_slowly("╗")

    for y in range(4):
        print_slowly("║", end = "") # price
        for x in range(4):
            print_slowly(prices[x][y], end = "")
            if x != 3:
                print_slowly("│", end = "")
            else:
                print_slowly("║")
        print_slowly("╟", end = "")
        for x in range(4):
            print_slowly("┈" * int(boxWidth / 4), end = "")
            if x != 3:
                print_slowly("┼", end = "")
            else:
                print_slowly("╢")

        for line in range(4):
            print_slowly("║", end = "")
            for x in range(4):
                print_slowly(tiles[line][x][y], end = "")
                for i in range(int(boxWidth / 4)  - len(tiles[line][x][y])): print_slowly(" ", end = "")
                if x != 3:
                    print_slowly("│", end = "")
                else:
                    print_slowly("║")

        print_slowly("║", end = "") # space for description
        for x in range(4):
            print_slowly(" " * int(boxWidth / 4), end = "")
            if x != 3:
                print_slowly("│", end = "")
            else:
                print_slowly("║")

        for line in range(4, 6):
            print_slowly("║", end = "")
            for x in range(4):
                print_slowly(tiles[line][x][y], end = "")
                #for i in range(int(boxWidth / 4)  - len(tiles[line][x][y])): print_slowly(" ", end = "")
                if x != 3:
                    print_slowly("│", end = "")
                else:
                    print_slowly("║")

        if y != 3:
            print_slowly("╟", end = "")
            for j in range(4):
                for i in range(int(boxWidth / 4)): print_slowly("─", end = "")
                if j != 3:
                    print_slowly("┼", end = "")
                else:
                    print_slowly("╢")

    print_slowly("╚", end = "")
    for j in range(4):
        for i in range(int(boxWidth / 4)): print_slowly("═", end = "")
        if j != 3:
            print_slowly("╧", end = "")
        else:
            print_slowly("╝")

def printVehicleStats(vehicle):
    print_slowly("╔", end = "")
    for i in range(boxWidth + 1): print_slowly("═", end = "")
    print_slowly("╗")
    
    tmp = [
        vehicle.name + ":", 
        str(vehicle.AP) + "/" + str(vehicle.maxAP) + " armor", 
        str(vehicle.acceleration) + " acceleration", 
        str(vehicle.handling) + " handling", 
        str(vehicle.braking) + " braking", 
        str(vehicle.capability) + " capability"]
    for j in range(6):
        print_slowly("║ ", end = "")
        print_slowly(tmp[j], end = "")
        for i in range(boxWidth - len(tmp[j])): print_slowly(" ", end = "")
        print_slowly("║")

    print_slowly("╚", end = "")
    for i in range(boxWidth + 1): print_slowly("═", end = "")
    print_slowly("╝")

def populateWorldTile(world, playerConvoy):
    tiles = [[0 for y in range(30)] for x in range(50)]
    for y in range(30):
        for x in range(50):
            if playerConvoy.x == x and playerConvoy.y == y:
                tiles[x][y] = "##"
            elif world.cityType[x][y] == 1:
                tiles[x][y] = "DM"
            elif world.cityType[x][y] == 2:
                tiles[x][y] = "CT"
            elif world.cityType[x][y] == 3:
                tiles[x][y] = "TW"
            elif world.terrain[x][y] == 0:
                tiles[x][y] = "██"
            elif world.terrain[x][y] == 1:
                tiles[x][y] = "▒▒"
            elif world.terrain[x][y] == 2:
                tiles[x][y] = "░░"
            elif world.terrain[x][y] == 3:
                tiles[x][y] = "╱╲"
            elif world.terrain[x][y] == 5:
                tiles[x][y] = "  "
    return tiles

def printWorld(world, playerConvoy):
    tiles = populateWorldTile(world, playerConvoy)

    print("╔", end = "")
    for i in range(100): print("═", end = "")
    print("╗")

    for y in range(30):
        print("║", end = "")
        for x in range(50):
            print(tiles[x][y], end = "")
        print("║")

    print("╟", end = "")
    for i in range(100): print("─", end = "")
    print("╢")

    legend1 = "║ ## = you, DM = Dome City, CT = City, TW = Town"
    print(legend1, end = "")
    for i in range(100 - len(legend1) + 1): print(" ", end = "")
    print("║")

    print("║", end = "")
    for i in range(100): print(" ", end = "")
    print("║")

    legend2 = "║ ██ = paved road, ▒▒ = dirt road, ░░ = rough terrain, ╱╲ = mountains"
    print(legend2, end = "")
    for i in range(100 - len(legend2) + 1): print(" ", end = "")
    print("║")

    print("║", end = "")
    for i in range(100): print(" ", end = "")
    print("║")

    legend3 = "║ ██ = -1 fuel, ▒▒ = -2 fuel, ░░ = -3 fuel, ╱╲ = -4 fuel (per vehicle)"
    print(legend3, end = "")
    for i in range(100 - len(legend3) + 1): print(" ", end = "")
    print("║")

    print("╚", end = "")
    for i in range(100): print("═", end = "")
    print("╝")

def printConvoy(convoy):
    printTextBox(convoy.name  + " has " + str(convoy.fuel) + " fuel & $" + str(convoy.money))
    printTextBox("Inventory:")
    printCargo(convoy)
    for i in range(4):
        if convoy.vehicles[i].name != "":
            printVehicleStats(convoy.vehicles[i])
            printUpgrades(convoy.vehicles[i])
            printWeapons(convoy.vehicles[i])

def printFrame():
    pass