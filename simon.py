"""
A Tkinter implementation of the classic `Simon` game
"""

import random
from functools import partial
from tkinter import Button, IntVar, Label, Tk
from typing import NamedTuple

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
        self.score: IntVar = IntVar()
        self.is_watching: int = True
        self.game_state: list[int] = []
        self.presses: int = 0

        Label(root, textvariable=self.score, font=("Courier", 25)).grid(
            padx=10, pady=2, row=0, columnspan=2
        )

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

    def press(self, button_index: int):
        """
        Call this function every time a button is pressed.
        `button_index` should refer to the button index of
        the pressed button in self.buttons.

        Return early if the press isn't correct.

        Increment the `presses` counter.

        If the amount of presses is equal to the number of
        presses in the current game state, increment the
        score and add another color to the current game
        state.
        """
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
            self.score.set(self.score.get() + 1)
            self.is_watching = True
            root.after(800, self.add_color)

    def add_color(self) -> None:
        """
        Add an additional color to the game state. Then,
        blink all of the colors in the state one at a time.
        """
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
    root.after(1000, Simon().add_color)
    root.mainloop()
