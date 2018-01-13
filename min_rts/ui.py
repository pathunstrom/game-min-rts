import logging

from ppb import Vector
from pygame import draw
from pygame import font as pgfont
from pygame import Surface
from pygame.sprite import DirtySprite

logger = logging.getLogger(__name__)


class Title(DirtySprite):

    def __init__(self, scene, title="Title", *groups, position=Vector(200, 75)):
        super().__init__(*groups)
        font = pgfont.Font(pgfont.get_default_font(), 36)
        self.image = font.render(title, True, (255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.dirty = 1
        self.scene = scene


class Button(DirtySprite):

    def __init__(self, scene, text="Button", position=Vector(300, 200), react=lambda: None, *groups):
        super().__init__(*groups)
        font = pgfont.Font(pgfont.get_default_font(), 22)
        text = font.render(text, True, (255, 255, 255))
        self.image = Surface((text.get_width() + 20, text.get_height() + 20))
        self.rect = self.image.get_rect()
        draw.rect(self.image, (255, 255, 255), self.rect, 3)
        text_rect = text.get_rect()
        text_rect.center = self.rect.center
        self.image.blit(text, text_rect)
        self.dirty = 1
        self.rect.center = position
        self.scene = scene
        self.state = listen
        self.react = react

    def update(self, *_):
        self.state(self)


def listen(actor):
    _logger = logger.getChild(listen.__qualname__)
    _logger.debug("Called")
    mouse = actor.scene.controller.mouse

    _logger.debug(mouse)
    if mouse.left_button.pressed and actor.rect.collidepoint(mouse.position):
        actor.state = wait


def wait(actor):
    _logger = logger.getChild(listen.__qualname__)
    _logger.debug("Called")
    mouse = actor.scene.controller.mouse

    _logger.debug(mouse)
    if not mouse.left_button.pressed:
        if actor.rect.collidepoint(mouse.position):
            actor.react()
        else:
            actor.state = listen
