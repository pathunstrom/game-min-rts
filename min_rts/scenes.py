from ppb import BaseScene
from ppb import Vector

from min_rts.controllers import Controller
from min_rts.ui import Button
from min_rts.ui import Title


class Game(BaseScene):

    def __init__(self, engine, background_color=(0, 0, 0)):
        super().__init__(engine, background_color=background_color)
        Title(self, "Game", self.groups["ui"])


class Menu(BaseScene):

    def __init__(self, engine, background_color=(0, 0, 0)):
        super().__init__(engine, background_color=background_color)
        self.rect = self.engine.display.get_rect()
        Title(self, "Minimum RTS", self.groups["ui"], position=Vector(self.rect.centerx, 75))
        Button(self, "Start", Vector(self.rect.centerx, self.rect.centery), self.prep_game, self.groups["ui"])
        self.controller = Controller()

    def simulate(self, time_delta: float):
        self.controller.update()
        super().simulate(time_delta)

    def prep_game(self):
        self.next = Game
        self.running = False
