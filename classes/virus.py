from classes.sprite import Sprite
from classes import constants
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
