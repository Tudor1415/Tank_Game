import arcade
import random as rd

class cmdMap:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
        self.map = self.generateMap()

    def initMap(self):
        return [[0 for _ in range(self.Y)] for i in range(self.X)]

    def generateMap(self):
        map = self.initMap()
        for i in range(self.X):
            map[i] = [rd.randint(0,1) for _ in range(self.Y)]
        return map

    def __str__(self):
        for i in range(self.X):
            print(self.map[i])
        return "Success"