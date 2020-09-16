from classes.player import Player
from classes.virus import Virus
import pyxel


class App:
    def __init__(self):
        pyxel.init(256, 150, caption='Corong', fps=60)
        self.player1 = Player('p1')
        self.player2 = Player('p2')
        self.virus = Virus(self.player1, self.player2)

        pyxel.load('assets/sprites.pyxres')
        pyxel.run(self.update, self.draw)

    def update(self):
        self.player1.update()
        self.player2.update()
        self.virus.update()

    def draw(self):
        pyxel.cls(0)
        self.player1.draw()
        self.player2.draw()
        self.virus.draw()


if __name__ == '__main__':
    App()
