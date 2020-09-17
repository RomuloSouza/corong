from classes.sprite import Sprite
from classes import constants
import random
import pyxel


class Virus(Sprite):
    def __init__(self):
        self.width = constants.VIRUS_WIDTH
        self.height = constants.VIRUS_HEIGHT
        self.img_idx = constants.VIRUS_IDX
        self.start_x = constants.VIRUS_START_X
        self.start_y = constants.VIRUS_START_Y
        self.pos_y = (pyxel.height - self.height) / 2
        self.pos_x = (pyxel.width - self.width) / 2

        self.speed_x = constants.VIRUS_MIN_SPEED_X
        self.speed_y = constants.VIRUS_MIN_SPEED_Y

    def update(self):
        self.pos_x += self.speed_x
        self.pos_y += int(self.speed_y)

        self.update_hitbox()

    def invert_speed_y_direction(self):
        self.speed_y *= -1

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
        self.pos_y = initial_height
        if initial_height:
            self.speed_y *= -1

        if player.name == 'p1':
            self.pos_x = player.syringe.width
        else:
            self.pos_x = pyxel.width - player.syringe.width
            self.speed_x *= -1
