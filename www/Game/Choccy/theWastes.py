# Main
# Osi's The Wastes

import UI
import loaders
import overworld

import world
import convoy
import vehicle
import weapon
import upgrade
import cargo

import random

world = world.world()
world.load("Assets/terrain.txt", "Assets/cities.txt")

shopVehicles = [vehicle.vehicle() for i in range(100)]
loaders.loadVehicles("Assets/shopVehicles.txt", shopVehicles)

enemyVehicles = [vehicle.vehicle() for i in range(100)]
loaders.loadVehicles("Assets/enemyVehicles.txt", enemyVehicles)

weapons = [weapon.weapon() for i in range(100)]
loaders.loadWeapons("Assets/weapons.txt", weapons)

upgrades = [upgrade.upgrade() for i in range(100)]
loaders.loadUpgrades("Assets/upgrades.txt", upgrades)

shooty1 = weapon.weapon() # setup procedure start
shooty1.name = "BigFuckinGun"
shooty1.damage = 100
shooty1.description = "*distant electric guitar plays*"
shooty2 = weapon.weapon()
shooty2.name = "lilCuteGun"
shooty2.damage = 50
shooty2.description = "aww!"

item1 = cargo.cargo()
item1.name = "encrypted data pack"
item1.destination = "Denver"
item1.awardForDelivery = 5000
item1.description = "Expensive data. Best not to ask questions."

item2 = cargo.cargo()
item2.name = "Rh null blood"
item2.destination = "Los Angeles"
item2.awardForDelivery = 20000
item2.description = "Special blood for a politian's sick child."

item3 = cargo.cargo()
item3.cargoWeapon = shooty1

item4 = cargo.cargo()
item4.cargoWeapon = shooty2

item5 = cargo.cargo()
item5.cargoUpgrade.name = "supercharger"
item5.cargoUpgrade.acceleration = 4
item5.cargoUpgrade.description = "\"whine noise\""
item5.cargoUpgrade.value = 150

item6 = cargo.cargo()
item6.cargoUpgrade.name = "Unobtainium Plate"
item6.cargoUpgrade.AP = 999
item6.cargoUpgrade.acceleration = -2
item6.cargoUpgrade.description = "It's made out of majics!"

jeep = vehicle.vehicle()
jeep.name = "Jeep"
jeep.baseMaxAP = 100
jeep.rightWeapon = shooty1
jeep.upWeapon = shooty2
jeep.upgrades[0] = item5.cargoUpgrade
jeep.resetAP()
jeep.AP -= 75
jeep.value = 99999

limo = vehicle.vehicle()
limo.name = "Limo"
limo.baseMaxAP = 100
limo.rightWeapon = shooty1
limo.downWeapon = shooty2
limo.upgrades[0] = item6.cargoUpgrade
limo.resetAP()
limo.AP -= 50
limo.value = 1

playerConvoy = convoy.convoy()
playerConvoy.name = "Player Convoy"
playerConvoy.vehicles[0] = jeep
playerConvoy.vehicles[1] = limo
playerConvoy.x = 48
playerConvoy.y = 6
playerConvoy.fuel = 99
playerConvoy.money = 1000
playerConvoy.cargo[0] = item1
playerConvoy.cargo[13] = item2
playerConvoy.cargo[14] = item3
playerConvoy.cargo[5] = item4
playerConvoy.cargo[10] = item5
"""
for x in range(100):
    if shopVehicles[x].name != "":
        print(shopVehicles[x].baseMaxAP)
        print(shopVehicles[x].baseAcceleration)
        print(shopVehicles[x].baseHandling)
        print(shopVehicles[x].baseBraking)
        print(shopVehicles[x].baseCapability)
        print(shopVehicles[x].value)
        print(shopVehicles[x].description)

for x in range(100):
    if upgrades[x].name != "":
        print(upgrades[x].name)
        print(upgrades[x].AP)
        print(upgrades[x].acceleration)
        print(upgrades[x].handling)
        print(upgrades[x].braking)
        print(upgrades[x].capability)
        print(upgrades[x].value)
        print(upgrades[x].description)

for x in range(100):
    if weapons[x].name != "":
        print(weapons[x].name)
        print(weapons[x].damage)
        print(weapons[x].value)
        print(weapons[x].description)
"""
# setup procedure end

print("\n" * 64)
UI.printTextBox("Get to LA!")
UI.printTextBox("Press [enter] to continue")
nuthin = input()

overworld.overworld(world, playerConvoy, shopVehicles, enemyVehicles, weapons, upgrades)