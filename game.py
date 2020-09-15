from classes.player import Player
import pyxel


class App:
    def __init__(self):
        pyxel.init(120, 90, caption='Corong', fps=30)
        self.player1 = Player('p1')
        self.player2 = Player('p2')

        pyxel.load('assets/syringe.pyxres')
        pyxel.run(self.update, self.draw)

    def update(self):
        self.player1.update()
        self.player2.update()

    def draw(self):
        pyxel.cls(0)
        self.player1.draw()
        self.player2.draw()


if __name__ == '__main__':
    App()
