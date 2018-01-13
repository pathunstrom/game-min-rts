from logging import DEBUG

from ppb import GameEngine

from min_rts.scenes import Menu

with GameEngine(Menu, log_level=DEBUG) as engine:
    engine.run()
