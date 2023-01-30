# convoy class
# Osi's The Wastes

import vehicle
import cargo

class convoy:
    def __init__(self, size = 0):
        self.name = ""

        self.x = 0
        self.y = 0

        self.vehicles = [vehicle.vehicle() for i in range(4)]
        self.size = size

        self.fuel = 0
        self.money = 0
        self.rations = 0

        self.cargo = [cargo.cargo() for i in range(16)]

        self.description = ""

    def getSize(self):
        index = 0
        for i in range(4):
            if self.vehicles[i].name != "":
                index = index + 1
        return index

    def setSize(self, value):
        return value

    size = property(getSize, setSize)
    
    def erase(self):
        self.name = ""

        for i in range(4):
            self.vehicles[i].erase

        self.size = 0

        self.fuel = 0
        self.money = 0
        self.rations = 0

        self.description = ""