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

    def __repr__(self):
        return f"{type(self).__name__}(_id={self.id}, pressed={self.pressed})"

    def __str__(self):
        return f"<{type(self).__name__}: id={self.id} pressed={self.pressed} held={self.held}>"


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

    def __str__(self):
        return f"{type(self).__name__}(left_button={self.left_button})"
