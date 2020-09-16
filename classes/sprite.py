import pyxel


class Sprite:
    def __init__(self):
        self.pos_x = 0
        self.pos_y = 0
        self.img_idx = 0

        # start (u, v) of the image bank (img_idx)
        self.start_x = 0
        self.start_y = 0

        self.width = 0
        self.height = 0

    def draw(self):
        pyxel.blt(
            self.pos_x,
            self.pos_y,
            self.img_idx,
            self.start_x,
            self.start_y,
            self.width,
            self.height,
            colkey=pyxel.COLOR_BLACK
        )
