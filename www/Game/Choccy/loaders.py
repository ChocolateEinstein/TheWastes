# loading functions
# Osi's The Wastes

import os
from pathlib import Path

def loadVehicles(fileName, vehicleList):
    dirname = os.path.dirname(__file__)
    filePath = os.path.join(dirname, fileName)

    rawVehicleList = open(filePath, "r")

    for i in range(100): 
        slice = rawVehicleList.readline().split(",")
        if slice[0] != "":
            vehicleList[i].name = slice[0]
            vehicleList[i].baseMaxAP = int(slice[1])
            vehicleList[i].resetAP()
            vehicleList[i].baseAcceleration = int(slice[2])
            vehicleList[i].baseHandling = int(slice[3])
            vehicleList[i].baseBraking = int(slice[4])
            vehicleList[i].baseCapability = int(slice[5])
            vehicleList[i].value = int(slice[6])
            vehicleList[i].description = slice[7]

    rawVehicleList.close()

def loadUpgrades(fileName, upgradeList):
    dirname = os.path.dirname(__file__)
    filePath = os.path.join(dirname, fileName)

    rawUpgradeList = open(filePath, "r")

    for i in range(100): 
        slice = rawUpgradeList.readline().split(",")
        if slice[0] != "":
            upgradeList[i].name = slice[0]
            upgradeList[i].AP = int(slice[1])
            upgradeList[i].acceleration = int(slice[2])
            upgradeList[i].handling = int(slice[3])
            upgradeList[i].braking = int(slice[4])
            upgradeList[i].capability = int(slice[5])
            upgradeList[i].value = int(slice[6])
            upgradeList[i].description = slice[7]

    rawUpgradeList.close()

def loadWeapons(fileName, weaponsList):
    dirname = os.path.dirname(__file__)
    filePath = os.path.join(dirname, fileName)

    rawWeaponsList = open(filePath, "r")

    for i in range(100): 
        slice = rawWeaponsList.readline().split(",")
        if slice[0] != "":
            weaponsList[i].name = slice[0]
            weaponsList[i].damage = int(slice[1])
            weaponsList[i].value = int(slice[2])
            weaponsList[i].description = slice[3]

    rawWeaponsList.close()