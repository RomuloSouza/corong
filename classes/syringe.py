from classes.sprite import Sprite
from classes import constants
import pyxel


class Syringe(Sprite):
    def __init__(self, name):
        self.width = constants.SYRINGE_WIDTH
        self.height = constants.SYRINGE_HEIGHT
        self.img_idx = constants.SYRINGE_IDX
        self.start_x = constants.SYRINGE_START_X
        self.start_y = constants.SYRINGE_START_Y
        self.pos_y = (pyxel.height - self.height) / 2

        if name == 'p1':
            self.pos_x = 0
            self.key_up = pyxel.KEY_W
            self.key_down = pyxel.KEY_S
        elif name == 'p2':
            self.pos_x = pyxel.width - self.width
            self.key_up = pyxel.KEY_UP
            self.key_down = pyxel.KEY_DOWN

    def update(self):
        if pyxel.btn(self.key_up) and self.pos_y > 0:
            self.pos_y -= constants.SYRINGE_SPEED

        elif pyxel.btn(self.key_down):
            if self.pos_y < pyxel.height-self.height:
                self.pos_y += constants.SYRINGE_SPEED
