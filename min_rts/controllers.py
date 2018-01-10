from ppb import Vector
from pygame import mouse


class Button:

    def __init__(self, _id, pressed=0):
        self.id = _id
        self.pressed = pressed
        self.held = False

    def update(self, pressed):
        if self.pressed and pressed:
            self.held = True
        else:
            self.held = False

        self.pressed = pressed


class Controller:

    def __init__(self):
        self.mouse = Mouse()

    def update(self):
        self.mouse.update()


class Mouse:

    def __init__(self):
        self.button_count = 0
        self.buttons = None
        self.position = Vector(0, 0)
        self.delta = Vector(0, 0)

    @property
    def left_button(self):
        return self.buttons[0]

    def update(self):
        position = Vector(*mouse.get_pos())
        self.delta = position - self.position
        self.position = position
        if self.buttons is None:
            self.buttons = tuple(Button(position, pressed) for position, pressed in enumerate(mouse.get_pressed()))
            return
        pressed = mouse.get_pressed()
        for button in self.buttons:
            button.update(pressed[button.id])


