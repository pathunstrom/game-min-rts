from ppb import GameEngine

from min_rts.scenes import Menu

with GameEngine(Menu) as engine:
    engine.run()