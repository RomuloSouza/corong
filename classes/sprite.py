import pyxel


class Sprite:
    def __init__(self, x, y, i, u, v, w, h):
        self.pos_x = x
        self.pos_y = y
        self.img_idx = i

        # start (u, v) of the image bank (img_idx)
        self.start_x = u
        self.start_y = v

        self.width = w
        self.height = h

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
