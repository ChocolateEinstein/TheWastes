# vehicle class
# Osi's The Wastes

import weapon
import upgrade

class vehicle:
    def __init__(self):
        self.name = ""

        self.x = 0
        self.y = 0

        self.AP = 0
        self.maxAP = 0

        self.baseMaxAP = 0

        self.wear = 0

        self.acceleration = 0
        self.handling = 0
        self.braking = 0
        self.capability = 0

        self.baseAcceleration = 0
        self.baseHandling = 0
        self.baseBraking = 0
        self.baseCapability = 0

        self.upWeapon = weapon.weapon()
        self.downWeapon = weapon.weapon()
        self.leftWeapon = weapon.weapon()
        self.rightWeapon = weapon.weapon()

        self.upgrades = [upgrade.upgrade() for i in range(4)]

        self.value = 0

        self.description = ""

    def getAPString(self):
        string = str(self.AP) + "/" + str(self.maxAP)
        return string

    def resetAP(self):
        self.AP = self.maxAP

    def getBaseMaxAP(self):
        tmp = self.baseMaxAP
        for i in range(4):
            tmp += self.upgrades[i].AP
        if tmp < 0:
            tmp = 0
        return tmp

    def getBaseAcceleration(self):
        tmp = self.baseAcceleration
        for i in range(4):
            tmp = tmp + self.upgrades[i].acceleration
        if tmp < 0:
            tmp = 0
        return tmp

    def getBaseHandling(self):
        tmp = self.baseHandling
        for i in range(4):
            tmp = tmp + self.upgrades[i].handling
        if tmp < 0:
            tmp = 0
        return tmp

    def getBaseBraking(self):
        tmp = self.baseBraking
        for i in range(4):
            tmp = tmp + self.upgrades[i].braking
        if tmp < 0:
            tmp = 0
        return tmp

    def getBaseCapability(self):
        tmp = self.baseCapability
        for i in range(4):
            tmp = tmp + self.upgrades[i].capability
        if tmp < 0:
            tmp = 0
        return tmp

    def setValue(self, newValue):
        return newValue

    maxAP = property(getBaseMaxAP, setValue)
    acceleration = property(getBaseAcceleration, setValue)
    handling = property(getBaseHandling, setValue)
    braking = property(getBaseBraking, setValue)
    capability = property(getBaseCapability, setValue)

    def erase(self):
        self.name = ""

        self.x = 0
        self.y = 0

        self.AP = 0
        self.maxAP = 0

        self.baseMaxAP = 0

        self.wear = 0

        self.acceleration = 0
        self.handling = 0
        self.braking = 0
        self.capability = 0

        self.baseAcceleration = 0
        self.baseHandling = 0
        self.baseBraking = 0
        self.baseCapability = 0

        self.upWeapon = weapon.weapon()
        self.downWeapon = weapon.weapon()
        self.leftWeapon = weapon.weapon()
        self.rightWeapon = weapon.weapon()

        self.value = 0

        self.description = ""