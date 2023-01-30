# world class
# Osi's The Wastes

import os

class world:
    def __init__(self):
        self.terrain = [[0 for y in range(30)] for x in range(50)] # [[0]*30]*50

        self.cityType = [[0 for y in range(30)] for x in range(50)]
        self.cityName = [["" for y in range(30)] for x in range(50)]

    def load(self, terrainFileName, cityFileName):
        dirname = os.path.dirname(__file__)
        terrainFilePath = os.path.join(dirname, terrainFileName)
        cityFilePath = os.path.join(dirname, cityFileName)

        rawTerrain = open(terrainFilePath)

        for y in range(30): 
            line = rawTerrain.readline().split(",")
            for x in range(50):
                self.terrain[x][y] = int(line[x])

        rawTerrain.close()

        rawCities = open(cityFilePath)

        for y in range(30): 
            line = rawCities.readline().split(",")
            for x in range(50):
                if line[x] != "!" and line[x] != "!\n":
                    city = line[x].split("@")
                    self.cityType[x][y] = int(city[0])
                    self.cityName[x][y] = city[1]

        rawCities.close()