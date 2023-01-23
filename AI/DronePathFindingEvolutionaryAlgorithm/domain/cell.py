

class Cell:
    def __init__(self, f, g, h, parentX, parentY):
        self.f = f
        self.g = g
        self.h = h
        self.parentX = parentX
        self.parentY = parentY
