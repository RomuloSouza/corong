import pyxel


class Score:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.last_to_score = None

    def draw(self):
        pyxel.text(
            pyxel.width / 2 - 20,
            0,
            str(self.player1.score),
            pyxel.COLOR_WHITE
        )

        pyxel.text(
            pyxel.width / 2 + 20,
            0,
            str(self.player2.score),
            pyxel.COLOR_WHITE
        )

    def increase_score(self, player):
        self.last_to_score = player
        player.score += 1
