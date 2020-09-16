from classes.sprite import Sprite
from classes import constants
import random
import pyxel


class Virus(Sprite):
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

        self.width = constants.VIRUS_WIDTH
        self.height = constants.VIRUS_HEIGHT
        self.img_idx = constants.VIRUS_IDX
        self.start_x = constants.VIRUS_START_X
        self.start_y = constants.VIRUS_START_Y
        self.pos_y = (pyxel.height - self.height) / 2
        self.pos_x = (pyxel.width - self.width) / 2

        self.speed_x = constants.VIRUS_MIN_SPEED_X
        self.speed_y = constants.VIRUS_MIN_SPEED_Y

        self.reset_virus(random.choice([player1, player2]))

    def update(self):
        self.pos_x += self.speed_x
        self.pos_y += int(self.speed_y)

        self.update_hitbox()

        self.check_screen_border()

        if self.speed_x > 0:
            if self.check_colision(self.player2):
                self.update_speed(self.player2)
        else:
            if self.check_colision(self.player1):
                self.update_speed(self.player1)

    def check_screen_border(self):
        if self.pos_y <= 0 or self.pos_y >= pyxel.height-self.width:
            self.speed_y *= -1

    def check_colision(self, player):
        for s_hbox in player.syringe.hitbox:
            if player.name == 'p1':
                v_hitbox = self.hitbox[0]
                if v_hitbox[0] > float(s_hbox[0]):
                    continue
            elif player.name == 'p2':
                v_hitbox = self.hitbox[1]
                if v_hitbox[0] < float(s_hbox[0]):
                    continue

            for v_hb in range(round(v_hitbox[1][0]), round(v_hitbox[1][1])):
                if s_hbox[1][0] <= v_hb <= s_hbox[1][1]:
                    return True

        return False

    def update_speed(self, player):
        both_up = self.speed_y < 0 and pyxel.btn(player.syringe.key_up)
        both_down = self.speed_y > 0 and pyxel.btn(player.syringe.key_down)
        if both_up or both_down:
            speed_min = min(abs(self.speed_x)+1, constants.VIRUS_MAX_SPEED_X)
            if self.speed_x < 0:
                self.speed_x = speed_min
            else:
                self.speed_x = -speed_min

            if self.speed_y < 0:
                self.speed_y -= 0.5
            else:
                self.speed_y += 0.5
        else:
            self.speed_x *= -1

    def update_hitbox(self):
        self.hitbox = [
            (self.pos_x+2, (self.pos_y+2, self.pos_y+2+4)),  # p1 colision
            (self.pos_x+self.width-2, (self.pos_y+2, self.pos_y+2+4))
        ]

    def reset_virus(self, player):
        initial_height = random.choice([0, pyxel.height-self.height])
        self.speed_x = constants.VIRUS_MIN_SPEED_X
        self.speed_y = constants.VIRUS_MIN_SPEED_Y
        if initial_height:
            self.speed_y *= -1

        if player.name == 'p1':
            self.pos_x = player.syringe.width
            self.pos_y = initial_height
        else:
            self.pos_x = pyxel.width - player.syringe.width
            self.pos_y = initial_height
            self.speed_x *= -1
