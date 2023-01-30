# overworld
# Osi's The Wastes

import UI
import loaders
import copy
import random

import world
import convoy
import vehicle
import weapon
import upgrade
import cargo

#shop \/
def findDistanceToCity(currentCity, destinationCity, world):
    for y in range(30):
                for x in range(50):
                    if world.cityName[x][y] == currentCity:
                        currentCityX = x
                        currentCityY = y
                    if world.cityName[x][y] == destinationCity:
                        destinationCityX = x
                        destinationCityY = y
    distance = pow(pow(currentCityX - destinationCityX, 2) + pow(currentCityY - destinationCityY, 2), 0.5) # distance formula with tiles as units
    return int(distance)

def populateMarketInv(currentCity, world, weapons, upgrades):
    marketInv = [cargo.cargo() for i in range(16)]

    for i in range(16):
        if  0 == random.randint(0, 1): # chance for slot to be populated, out of 3
            chance = random.randint(0, 100)
            item = cargo.cargo()

            chancePackage = 50 # out of 100
            chanceUpgrade = 50 # out of 100
            chanceWeapon = 100 - (chancePackage + chanceUpgrade) # remainder

            cities = []
            newCity = [""]
            index = 0
            for y in range(30):
                for x in range(50):
                    if world.cityType[x][y] > 0:
                        newCity[0] = world.cityName[x][y]
                        cities += newCity

            if chance < chancePackage: # chance for slot to be populated with a package
                item.name = "amazon package"
                item.destination = random.choice(cities)
                distance = findDistanceToCity(currentCity, item.destination, world)
                item.awardForDelivery = distance * 10
                item.description = "pretty big box"
            elif chance < chancePackage + chanceUpgrade: # chance for slot to be populated with an upgrade
                while item.cargoUpgrade.name == "":
                    item.cargoUpgrade = copy.deepcopy(random.choice(upgrades))
            else: # otherwise get populated with a weapon
                while item.cargoWeapon.name == "":
                    item.cargoWeapon = copy.deepcopy(random.choice(weapons))

            marketInv[i] = copy.deepcopy(item)
            item.erase()    

    return marketInv

def populateMarketLot(currentCity, world, shopVehicles):
    marketLot = [vehicle.vehicle() for i in range(4)]

    for i in range(4):
        if  0 == random.randint(0, 1): # chance for slot to be populated, out of 3
            while marketLot[i].name == "":
                marketLot[i] = copy.deepcopy(random.choice(shopVehicles))

    return marketLot

def buyItem(playerConvoy, marketInv):
    index = 0
    for i in range(4):
        if playerConvoy.cargo[i].content != "empty":
            index += 1
    if index == 16:
        UI.printTextBox("Inventory full!")
        return

    print("\n" * 4)

    while True:
        UI.printTextBox("Market Inventory:")
        UI.printMarketInv(marketInv)
        UI.printTextBox("Buy which item?")
        tmpChoice = input()
        if tmpChoice == "":
            tmpChoice = "-1"
        choice = int(tmpChoice)

        if (1 <= choice and choice <= 16) and (marketInv[choice - 1].content != "empty"):
            if marketInv[choice - 1].content == "package":
                itemValue = 100 # cost for package
                itemName = "package" # what to call package
            elif marketInv[choice - 1].content == "upgrade":
                itemValue = marketInv[choice - 1].cargoUpgrade.value
                itemName = marketInv[choice - 1].cargoUpgrade.name
            elif marketInv[choice - 1].content == "weapon":
                itemValue = marketInv[choice - 1].cargoWeapon.value
                itemName = marketInv[choice - 1].cargoWeapon.name

            if itemValue <= playerConvoy.money:
                for i in range(16):
                    if (playerConvoy.cargo[i].content == "empty"):
                        playerConvoy.cargo[i] = copy.deepcopy(marketInv[choice - 1])
                        playerConvoy.money -= itemValue
                        marketInv[choice - 1].erase()
                        UI.printTextBox("You bought the " + itemName + " for $" + str(itemValue))
                        UI.printTextBox("You now have $" + str(playerConvoy.money))
                        UI.printTextBox("Press [enter] to continue")
                        nuthin = input()
                        print("\n" * 4)
                        return
            else:
                UI.printTextBox("You can't afford that.")
                UI.printTextBox("Press [enter] to continue")
                nuthin = input()
                return

        else:
            UI.printTextBox("Invalid input")
            return

def buyFuel(playerConvoy, fuelPrice):
    print("\n" * 4)

    UI.printTextBox("Cost to navigate per tile, per vehicle:")
    UI.printTextBox("██ = -1 fuel, ▒▒ = -2 fuel, ░░ = -3 fuel, ╱╲ = -4 fuel")
    UI.printTextBox("Fuel costs $" + str(fuelPrice) + " per unit here. You currently have " + str(playerConvoy.fuel) + " fuel and $" + str(playerConvoy.money))
    UI.printTextBox("How much fuel do you want to buy?")
    
    tmpChoice = input()
    if tmpChoice == "":
        tmpChoice = "-1"
    choice = int(tmpChoice)

    if choice > 0:
        if (choice * fuelPrice) <= playerConvoy.money:
            playerConvoy.money -= choice * fuelPrice
            playerConvoy.fuel += choice
            UI.printTextBox("Purchaced " + str(choice) + " fuel for $" + str(choice * fuelPrice))
            UI.printTextBox("You currently have " + str(playerConvoy.fuel) + " fuel and $" + str(playerConvoy.money))
            UI.printTextBox("Press [enter] to continue")
            nuthin = input()
            return
        else:
            UI.printTextBox("You do not have enough money to buy $" + str(choice * fuelPrice) + " of fuel.")
            UI.printTextBox("Press [enter] to continue")
            nuthin = input()
            return
    else:
        UI.printTextBox("Invalid input")
        UI.printTextBox("Press [enter] to continue")
        nuthin = input()
        return

def buyVehicle(playerConvoy, marketLot):
    if playerConvoy.size >= 4:
        UI.printTextBox("Convoy full!")
        UI.printTextBox("Press [enter] to continue")
        nuthin = input()
        return

    found = 0
    for i in range(4):
        if marketLot[i].name != "":
            found += 1
    if found == 0:
        UI.printTextBox("No vehicles available for sale right now.")
        UI.printTextBox("Press [enter] to continue")
        nuthin = input()
        return

    print("\n" * 4)

    while True:
        UI.printTextBox("Market Lot:")
        for i in range(4):
            if marketLot[i].name != "":
                print("\n")
                UI.printTextBox(str(i + 1) + ". $" + str(marketLot[i].value))
                UI.printVehicleStats(marketLot[i])
        UI.printTextBox("Buy which vehicle?")
        tmpChoice = input()
        if tmpChoice == "":
            tmpChoice = "-1"
        choice = int(tmpChoice)

        if (1 <= choice and choice <= 4) and (marketLot[choice - 1].name != ""):
            if marketLot[choice - 1].value <= playerConvoy.money:
                for i in range(4):
                    if (playerConvoy.vehicles[i].name == ""):
                        UI.printTextBox("You bought the " + marketLot[choice - 1].name + " for $" + str(marketLot[choice - 1].value))
                        playerConvoy.vehicles[i] = copy.deepcopy(marketLot[choice - 1])
                        playerConvoy.money -= marketLot[choice - 1].value
                        marketLot[choice - 1].erase()
                        UI.printTextBox("You now have $" + str(playerConvoy.money))
                        UI.printTextBox("Press [enter] to continue")
                        nuthin = input()
                        print("\n" * 4)
                        return
            else:
                UI.printTextBox("You can't afford that.")
                UI.printTextBox("Press [enter] to continue")
                nuthin = input()
                return

        else:
            UI.printTextBox("Invalid input")
            return

def shop(world, playerConvoy, marketInv, marketLot):
    print("\n" * 4)

    fuelPrice = world.cityType[playerConvoy.x][playerConvoy.y] # fuel price math

    while True:
        UI.printTextBox("Fuel costs $" + str(fuelPrice) + "/unit")
        options = ["Buy item", "Buy fuel", "Buy vehicle", "", "Check inventory", "Leave shop"]
        UI.printHexMenu(options)
        tmpChoice = input()
        if tmpChoice == "":
            tmpChoice = "-1"
        choice = int(tmpChoice)

        if choice == 1:
            buyItem(playerConvoy, marketInv)
        elif choice == 2:
            buyFuel(playerConvoy, fuelPrice)
        elif choice == 3:
            buyVehicle(playerConvoy, marketLot)
        elif choice == 5:
            UI.printTextBox("Inventory:")
            UI.printConvoy(playerConvoy)
        elif choice == 6:
            return
        else:
            UI.printTextBox("Invalid input")

def sellItem(world, playerConvoy):
    print("\n" * 4)

    while True:
        value = 0
        UI.printTextBox("Inventory:")
        UI.printMarketInv(playerConvoy.cargo)
        UI.printTextBox("You have $" + str(playerConvoy.money) + ".")
        UI.printTextBox("What to sell?")
        tmpChoice = input()
        if tmpChoice == "":
            tmpChoice = "-1"
        choice = int(tmpChoice)

        if (1 <= choice and choice <= 16) and (playerConvoy.cargo[choice - 1].content != "empty"):
            if playerConvoy.cargo[choice - 1].content == "package":
                if playerConvoy.cargo[choice - 1].destination != world.cityName[playerConvoy.x][playerConvoy.y]:
                    UI.printTextBox("You must deliver the package to the correct city!")
                    UI.printTextBox("Press [enter] to continue")
                    nuthin = input()
                    return
                value = playerConvoy.cargo[choice - 1].awardForDelivery
                UI.printTextBox("Delivered package for $" + str(value))
            elif playerConvoy.cargo[choice - 1].content == "upgrade":
                value = playerConvoy.cargo[choice - 1].cargoUpgrade.value
                UI.printTextBox("Sold for $" + str(value))
            elif playerConvoy.cargo[choice - 1].content == "weapon":
                value = playerConvoy.cargo[choice - 1].cargoWeapon.value
                UI.printTextBox("Sold for $" + str(value))
            
            playerConvoy.money += value
            UI.printTextBox("You now have $" + str(playerConvoy.money))
            playerConvoy.cargo[choice - 1].erase()
            UI.printTextBox("Press [enter] to continue")
            nuthin = input()
            return
        else:
            UI.printTextBox("Invalid input")

def sellVehicle(playerConvoy):
    print("\n" * 4)

    UI.printTextBox("Your vehicles (UPGRADES AND WEAPONS INCLUDED):")
    for i in range(4):
        if playerConvoy.vehicles[i].name != "":
            print("\n")
            UI.printTextBox(str(i + 1) + ". $" + str(playerConvoy.vehicles[i].value))
            UI.printVehicleStats(playerConvoy.vehicles[i])
    UI.printTextBox("Sell which vehicle?")
    tmpChoice = input()
    if tmpChoice == "":
        tmpChoice = "-1"
    choice = int(tmpChoice)

    if (1 <= choice and choice <= 4) and (playerConvoy.vehicles[choice - 1].name != ""):
        UI.printTextBox("You sold the " + playerConvoy.vehicles[choice - 1].name + " for $" + str(playerConvoy.vehicles[choice - 1].value))
        playerConvoy.money += playerConvoy.vehicles[choice - 1].value
        playerConvoy.vehicles[choice - 1].erase()
        UI.printTextBox("You now have $" + str(playerConvoy.money))
        UI.printTextBox("Press [enter] to continue")
        nuthin = input()
        print("\n" * 4)
        return
    else:
        UI.printTextBox("Invalid input")
        return

def market(world, playerConvoy, marketInv, marketLot):
    print("\n" * 4)

    while True:
        UI.printTextBox("Market")
        options = ["Shop", "Sell item / deliver package", "Sell vehicles", "", "Check inventory", "Leave shop"]
        UI.printHexMenu(options)
        tmpChoice = input()
        if tmpChoice == "":
            tmpChoice = "-1"
        choice = int(tmpChoice)

        if choice == 1:
            shop(world, playerConvoy, marketInv, marketLot)
        elif choice == 2:
            sellItem(world, playerConvoy)
        elif choice == 3:
            sellVehicle(playerConvoy)
        elif choice == 5:
            UI.printTextBox("Inventory:")
            UI.printConvoy(playerConvoy)
        elif choice == 6:
            return
        else:
            UI.printTextBox("Invalid input")

#garage \/
def installUpgrade(vehicle, playerConvoy):
    index = 0
    for i in range(4):
        if vehicle.upgrades[i].name != "":
            index += 1
    if index == 4:
        UI.printTextBox("Upgrades full!")
        return

    print("\n" * 4)

    while True:
        UI.printCargo(playerConvoy)
        UI.printTextBox("Install which upgrade?")
        tmpChoice = input()
        if tmpChoice == "":
            tmpChoice = "-1"
        choice = int(tmpChoice)

        if (1 <= choice and choice <= 16) and (playerConvoy.cargo[choice - 1].content == "upgrade"):
            for i in range(4):
                if vehicle.upgrades[i].name == "":
                    vehicle.upgrades[i] = copy.deepcopy(playerConvoy.cargo[choice - 1].cargoUpgrade)
                    playerConvoy.cargo[choice - 1].erase()
                    UI.printTextBox("Upgrade installed:")
                    UI.printUpgrades(vehicle)
                    UI.printTextBox("Press [enter] to continue")
                    nuthin = input()
                    print("\n" * 4)
                    return
        else:
            UI.printTextBox("Invalid input")
            return

def removeUpgrade(vehicle, playerConvoy):
    index = 0
    for i in range(16):
        if playerConvoy.cargo[i].content != "empty":
            index += 1
    if index == 16:
        UI.printTextBox("Inventory full!")
        return

    print("\n" * 4)

    while True:
        UI.printUpgrades(vehicle)
        UI.printTextBox("Remove which upgrade?")
        tmpChoice = input()
        if tmpChoice == "":
            tmpChoice = "-1"
        choice = int(tmpChoice)

        if (1 <= choice and choice <= 4) and (vehicle.upgrades[choice - 1].name != ""):
            removed = 0
            j = 0
            while removed == 0:
                if playerConvoy.cargo[j].content == "empty":
                    playerConvoy.cargo[j].cargoUpgrade = copy.deepcopy(vehicle.upgrades[choice - 1])
                    vehicle.upgrades[choice - 1].erase()
                    removed = 1
                j += 1
            print("\n" * 4)
            UI.printTextBox("Upgrade removed from vehicle:")
            UI.printUpgrades(vehicle)
            UI.printTextBox("and placed in your inventory:")
            UI.printCargo(playerConvoy)
            UI.printTextBox("Press [enter] to continue")
            nuthin = input()
            print("\n" * 4)
            return
        else:
            UI.printTextBox("Invalid input")
            return

def installWeapon(vehicle, playerConvoy):
    print("\n" * 4)

    while True:
        UI.printCargo(playerConvoy)
        UI.printWeapons(vehicle)
        UI.printTextBox("Install which weapon?")
        tmpChoice = input()
        if tmpChoice == "":
            tmpChoice = "-1"
        choiceCargo = int(tmpChoice)

        UI.printTextBox("Into which slot?")
        tmpChoice = input()
        if tmpChoice == "":
            tmpChoice = "-1"
        choiceWeapon = int(tmpChoice)

        if choiceWeapon == 1:
            if (1 <= choiceCargo and choiceCargo <= 16) and (playerConvoy.cargo[choiceCargo - 1].content == "weapon"):
                if vehicle.upWeapon.name == "":
                    vehicle.upWeapon = copy.deepcopy(playerConvoy.cargo[choiceCargo - 1].cargoWeapon)
                    playerConvoy.cargo[choiceCargo - 1].erase()
                    UI.printTextBox("Weapon installed:")
                    UI.printWeapons(vehicle)
                    UI.printTextBox("Press [enter] to continue")
                    nuthin = input()
                    print("\n" * 4)
                    return
                else:
                    UI.printTextBox("Weapon slot full!")
                    return
        elif choiceWeapon == 2:
            if (1 <= choiceCargo and choiceCargo <= 16) and (playerConvoy.cargo[choiceCargo - 1].content == "weapon"):
                if vehicle.downWeapon.name == "":
                    vehicle.downWeapon = copy.deepcopy(playerConvoy.cargo[choiceCargo - 1].cargoWeapon)
                    playerConvoy.cargo[choiceCargo - 1].erase()
                    UI.printTextBox("Weapon installed:")
                    UI.printWeapons(vehicle)
                    UI.printTextBox("Press [enter] to continue")
                    nuthin = input()
                    return
                else:
                    UI.printTextBox("Weapon slot full!")
                    return
        elif choiceWeapon == 3:
            if (1 <= choiceCargo and choiceCargo <= 16) and (playerConvoy.cargo[choiceCargo].content == "weapon"):
                if vehicle.leftWeapon.name == "":
                    vehicle.leftWeapon = copy.deepcopy(playerConvoy.cargo[choiceCargo - 1].cargoWeapon)
                    playerConvoy.cargo[choiceCargo - 1].erase()
                    UI.printTextBox("Weapon installed:")
                    UI.printWeapons(vehicle)
                    UI.printTextBox("Press [enter] to continue")
                    nuthin = input()
                    return
                else:
                    UI.printTextBox("Weapon slot full!")
                    return
        elif choiceWeapon == 3:
            if (1 <= choiceCargo and choiceCargo <= 16) and (playerConvoy.cargo[choiceCargo - 1].content == "weapon"):
                if vehicle.rightWeapon.name == "":
                    vehicle.rightWeapon = copy.deepcopy(playerConvoy.cargo[choiceCargo - 1].cargoWeapon)
                    playerConvoy.cargo[choiceCargo - 1].erase()
                    UI.printTextBox("Weapon installed:")
                    UI.printWeapons(vehicle)
                    UI.printTextBox("Press [enter] to continue")
                    nuthin = input()
                    return
                else:
                    UI.printTextBox("Weapon slot full!")
                    return
        else:
            UI.printTextBox("Invalid input")
            return

def removeWeapon(vehicle, playerConvoy):
    index = 0
    for i in range(16):
        if playerConvoy.cargo[i].name != "":
            index = index + 1
    if index == 16:
        UI.printTextBox("Inventory full!")
        return

    print("\n" * 4)

    while True:
        UI.printWeapons(vehicle)
        UI.printTextBox("Remove which Weapon?")
        tmpChoice = input()
        if tmpChoice == "":
            tmpChoice = "-1"
        choice = int(tmpChoice)

        if (1 <= choice and choice <= 4) and choice == 1:
            if vehicle.upgrades[choice - 1].content != "empty":
                for i in range(16):
                    if playerConvoy.cargo[i].content == "empty":
                        playerConvoy.cargo[i].cargoWeapon = copy.deepcopy(vehicle.upWeapon)
                vehicle.upWeapon.erase()
                UI.printTextBox("Weapon removed:")
                UI.printWeapons(vehicle)
                UI.printTextBox("Press [enter] to continue")
                nuthin = input()
                print("\n" * 4)
                return
        if (1 <= choice and choice <= 4) and choice == 2:
            if vehicle.upgrades[choice - 1].content != "empty":
                for i in range(16):
                    if playerConvoy.cargo[i].content == "empty":
                        playerConvoy.cargo[i].cargoWeapon = copy.deepcopy(vehicle.downWeapon)
                vehicle.downWeapon.erase()
                UI.printTextBox("Weapon removed:")
                UI.printWeapons(vehicle)
                UI.printTextBox("Press [enter] to continue")
                nuthin = input()
                print("\n" * 4)
                return
        if (1 <= choice and choice <= 4) and choice == 3:
            if vehicle.upgrades[choice - 1].content != "empty":
                for i in range(16):
                    if playerConvoy.cargo[i].content == "empty":
                        playerConvoy.cargo[i].cargoWeapon = copy.deepcopy(vehicle.leftWeapon)
                vehicle.leftWeapon.erase()
                UI.printTextBox("Weapon removed:")
                UI.printWeapons(vehicle)
                UI.printTextBox("Press [enter] to continue")
                nuthin = input()
                print("\n" * 4)
                return
        if (1 <= choice and choice <= 4) and choice == 4:
            if vehicle.upgrades[choice - 1].content != "empty":
                for i in range(16):
                    if playerConvoy.cargo[i].content == "empty":
                        playerConvoy.cargo[i].cargoWeapon = copy.deepcopy(vehicle.rightWeapon)
                vehicle.rightWeapon.erase()
                UI.printTextBox("Weapon removed:")
                UI.printWeapons(vehicle)
                UI.printTextBox("Press [enter] to continue")
                nuthin = input()
                print("\n" * 4)
                return
        else:
            UI.printTextBox("Invalid input")
            return

def modifyVehicleMenuMenu(vehicle, playerConvoy):
    print("\n" * 4)

    while True:
        UI.printVehicleStats(vehicle)
        UI.printUpgrades(vehicle)
        UI.printWeapons(vehicle)
        UI.printTextBox("Modify what aspect?")

        options = ["Install upgrade", "Remove Upgrade", "Install weapon", "Remove weapon", "", "Back"]
        UI.printHexMenu(options)
        tmpChoice = input()
        if tmpChoice == "":
            tmpChoice = "-1"
        choice = int(tmpChoice)

        if choice == 6:
            print("\n" * 4)
            return
        elif choice == 1:
            installUpgrade(vehicle, playerConvoy)
            return
        elif choice == 2:
            removeUpgrade(vehicle, playerConvoy)
            return
        elif choice == 3:
            installWeapon(vehicle, playerConvoy)
            return
        elif choice == 4:
            removeWeapon(vehicle, playerConvoy)
            return
        else:
            UI.printTextBox("Invalid input")

def modifyVehicleMenu(playerConvoy):
    print("\n" * 4)

    while True:
        UI.printConvoy(playerConvoy)

        UI.printTextBox("Modify which vehicle?")
        options = ["", "", "", "", "", "Back"]
        for i in range(4):
            if playerConvoy.vehicles[i].name != "":
                options[i] = playerConvoy.vehicles[i].name
        UI.printHexMenu(options)
        tmpChoice = input()
        if tmpChoice == "":
            tmpChoice = "-1"
        choice = int(tmpChoice)

        if choice == 6:
            print("\n" * 4)
            return
        elif choice == 1 or 2 or 3 or 4:
            modifyVehicleMenuMenu(playerConvoy.vehicles[choice - 1], playerConvoy)
            return
        else:
            UI.printTextBox("Invalid input")

def repair(world, playerConvoy):
    repairPrice = 10 #repairPrice/AP

    print("\n" * 4)

    while True:
        armorDamage = [0 for i in range(4)] #determine nessicary repairs
        allArmorDamage = 0
        for i in range(4):
            armorDamage[i] = playerConvoy.vehicles[i].maxAP - playerConvoy.vehicles[i].AP
            allArmorDamage = allArmorDamage + armorDamage[i]

        repairCost = [0 for i in range(4)] #determine nessicary repairs
        allRepairCost = 0
        if world.cityType[playerConvoy.x][playerConvoy.y] == 1: #determine cost of repairs
            repairPrice = int(repairPrice / 1)
        elif world.cityType[playerConvoy.x][playerConvoy.y] == 2:
            repairPrice = int(repairPrice / 2)
        elif world.cityType[playerConvoy.x][playerConvoy.y] == 3:
            repairPrice = int(repairPrice / 3)
        for i in range(4):
            repairCost[i] = int(armorDamage[i] * repairPrice)
            allRepairCost = allRepairCost + repairCost[i]

        UI.printTextBox("Repair which vehicle? You have $" + str(playerConvoy.money) + ".")
        options = ["Repair all ($" + str(allRepairCost) + ")", "", "", "", "", "Back"]
        for i in range(4):
            if playerConvoy.vehicles[i].name != "":
                options[i + 1] = playerConvoy.vehicles[i].name + " " + playerConvoy.vehicles[i].getAPString() + " ($" + str(repairCost[i]) + ")"
        UI.printHexMenu(options)
        tmpChoice = input()
        if tmpChoice == "":
            tmpChoice = "-1"
        choice = int(tmpChoice)

        if choice == 6:
            print("\n" * 4)
            return
        elif choice == 1:
            if allRepairCost <= playerConvoy.money:
                playerConvoy.money = playerConvoy.money - allRepairCost
                for v in playerConvoy.vehicles:
                    v.resetAP()
                return
            else:
                UI.printTextBox("Insufficient Money") 
        elif choice == 2 or 3 or 4 or 5:
            if repairCost[choice - 2] <= playerConvoy.money:
                playerConvoy.money = playerConvoy.money - repairCost[choice - 2]
                playerConvoy.vehicles[choice - 2].resetAP()
            else:
                UI.printTextBox("Insufficient Money")
        else:
            UI.printTextBox("Invalid input")

def garage(world, playerConvoy):
    print("\n" * 4)

    while True:
        UI.printTextBox("Garage")

        options = ["Repair vehicles", "Modify vehicles", "Check inventory", "Leave garage"]
        UI.printQuadMenu(options)
        tmpChoice = input()
        if tmpChoice == "":
            tmpChoice = "-1"
        choice = int(tmpChoice)

        if choice == 1:
            repair(world, playerConvoy)
        elif choice == 2:
            modifyVehicleMenu(playerConvoy)
        elif choice == 3:
            UI.printTextBox("Inventory:")
            UI.printConvoy(playerConvoy)
        elif choice == 4:
            print("\n" * 4)
            return
        else:
            UI.printTextBox("Invalid input")

#main \/
def city(world, playerConvoy, shopVehicles, weapons, upgrades):
    print("\n" * 4)

    marketInv = populateMarketInv(world.cityName[playerConvoy.x][playerConvoy.y], world, weapons, upgrades)
    marketLot = populateMarketLot(world.cityName[playerConvoy.x][playerConvoy.y], world, shopVehicles)    

    UI.printTextBox("Welcome to " + world.cityName[playerConvoy.x][playerConvoy.y] + "!")
    UI.printTextBox("Press [enter] to continue")
    nuthin = input()

    while True:
        UI.printTextBox("What do you want to do?")
        UI.printTextBox("You have " + str(playerConvoy.fuel) + " fuel and $" + str(playerConvoy.money) + ".")

        options = ["Garage", "Market", "Check inventory", "Leave"]
        UI.printQuadMenu(options)
        tmpChoice = input()
        if tmpChoice == "":
            tmpChoice = "-1"
        choice = int(tmpChoice)

        if choice == 1:
            garage(world, playerConvoy)
        elif choice == 2:
            market(world, playerConvoy, marketInv, marketLot)
        elif choice == 3:
            UI.printTextBox("Inventory:")
            UI.printConvoy(playerConvoy)
        elif choice == 4:
            print("\n" * 4)
            return
        else:
            UI.printTextBox("Invalid input")

    UI.printTextBox("Press [enter] to continue")
    nuthin = input()