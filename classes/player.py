from classes.syringe import Syringe


class Player:
    def __init__(self, name):
        self.score = 0
        self.name = name
        self.syringe = Syringe(self.name)

    def draw(self):
        self.syringe.draw()

    def update(self):
        self.syringe.update()
