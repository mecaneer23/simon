"""
A Tkinter implementation of the classic `Simon` game
"""

from tkinter import Tk, Label, Button
from functools import partial
from typing import NamedTuple
import random

root = Tk()
root.title("Simon")


class Color(NamedTuple):
    """Represent a color in terms of a name and hexadecimal shade"""

    name: str
    shade: str


COLORS: list[Color] = [
    Color("green", "#003300"),
    Color("red", "#550000"),
    Color("yellow", "#555500"),
    Color("blue", "#000055"),
]


class Simon:
    """The classic Simon game"""

    def __init__(self):
        self.score: int = 0
        self.is_watching: int = True
        self.game_state: list[int] = []
        self.presses: int = 0

        self.score_label = Label(root, text="0", font=("Courier", 25))
        self.score_label.grid(padx=10, pady=2, row=0, columnspan=2)

        Label(root, text="WATCH first, PLAY after").grid(
            padx=10, pady=2, row=1, columnspan=2
        )

        self.buttons: list[Button] = []
        for index, color in enumerate(COLORS):
            button = Button(
                root,
                text="",
                bg=color.shade,
                activebackground=color.name,
                width=8,
                height=6,
                command=partial(self.press, index),
            )
            self.buttons.append(button)
            button.grid(padx=5, pady=10, row=index // 2 + 2, column=index % 2)

    def press(self, button_index: int = 0):
        if (
            len(self.game_state) > 0
            and not self.is_watching
            and self.game_state[self.presses] != button_index
        ):
            root.destroy()
            return

        self.presses += 1
        if self.presses == len(self.game_state):
            self.presses = 0
            self.score += 1
            self.score_label.config(text=self.score)
            self.is_watching = True
            root.after(800, self.add_color)

    def add_color(self) -> None:
        self.game_state.append(random.randint(0, 3))
        timer_count = 0
        for color in self.game_state:
            root.after(timer_count, lambda: None)
            root.after(
                timer_count + 300,
                partial(self.buttons[color].config, bg=COLORS[color].name),
            )
            root.after(
                timer_count + 500,
                partial(self.buttons[color].config, bg=COLORS[color].shade),
            )

            timer_count += 800
        self.is_watching = False


if __name__ == "__main__":
    game = Simon()
    root.after(1000, game.add_color)
    root.mainloop()
