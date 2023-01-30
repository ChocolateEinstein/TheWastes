# cargo class
# Osi's The Wastes

import weapon
import upgrade

class cargo:
    def __init__(self):
        self.name = ""

        self.cargoWeapon = weapon.weapon()
        self.cargoUpgrade = upgrade.upgrade()

        self.destination = ""
        self.awardForDelivery = 0

        self.description = ""

    @property
    def content(self):
        if self.cargoUpgrade.name != "":
            return "upgrade"
        elif self.cargoWeapon.name != "":
            return "weapon"
        elif self.name != "":
            return "package"
        else:
            return "empty"
            
    def erase(self):
        self.name = ""

        self.cargoWeapon.erase()
        self.cargoUpgrade.erase()

        self.destination = ""
        self.awardForDelivery = 0

        self.description = ""