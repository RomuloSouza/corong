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

        self.speed_x = 0
        self.speed_y = 0

        self.hitbox = [
            (self.pos_x+2, (self.pos_y+2, self.pos_y+4)),
            (self.pos_x+self.width-2, (self.pos_y+2, self.pos_y+4))
        ]

        self.initial_setup(random.choice([player1, player2]))

    def update(self):
        self.pos_x += self.speed_x
        self.pos_y += self.speed_y

    def check_colision(self):
        ...

    def initial_setup(self, player):
        initial_height = random.choice([0, pyxel.height-self.height])
        self.speed_x = constants.VIRUS_SPEED_X
        self.speed_y = constants.VIRUS_SPEED_Y
        if initial_height:
            self.speed_y *= -1

        if player.name == 'p1':
            self.pos_x = player.syringe.width
            self.pos_y = initial_height
        else:
            self.pos_x = pyxel.width - player.syringe.width
            self.pos_y = initial_height
            self.speed_x *= -1
