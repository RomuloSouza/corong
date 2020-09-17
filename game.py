from classes.player import Player
from classes.virus import Virus
import random
import pyxel


class App:
    def __init__(self):
        pyxel.init(256, 150, caption='Corong', fps=60)
        self.player1 = Player('p1')
        self.player2 = Player('p2')

        self.virus = Virus()
        self.virus.reset_virus(random.choice([self.player1, self.player2]))

        pyxel.load('assets/sprites.pyxres')
        pyxel.run(self.update, self.draw)

    def update(self):
        self.player1.update()
        self.player2.update()
        self.virus.update()

        self.check_screen_border()

        if self.virus.speed_x > 0:
            if self.check_colision(self.player2):
                self.virus.update_speed(self.player2)
        else:
            if self.check_colision(self.player1):
                self.virus.update_speed(self.player1)

    def draw(self):
        pyxel.cls(0)
        self.player1.draw()
        self.player2.draw()
        self.virus.draw()

    def check_screen_border(self):
        virus = self.virus
        if virus.pos_y <= 0 or virus.pos_y >= pyxel.height-virus.width:
            virus.invert_speed_y_direction()

    def check_colision(self, player):
        for s_hbox in player.syringe.hitbox:
            if player.name == 'p1':
                v_hitbox = self.virus.hitbox[0]
                if v_hitbox[0] > float(s_hbox[0]):
                    continue
            elif player.name == 'p2':
                v_hitbox = self.virus.hitbox[1]
                if v_hitbox[0] < float(s_hbox[0]):
                    continue

            for v_hb in range(round(v_hitbox[1][0]), round(v_hitbox[1][1])):
                if s_hbox[1][0] <= v_hb <= s_hbox[1][1]:
                    return True

        return False


if __name__ == '__main__':
    App()
