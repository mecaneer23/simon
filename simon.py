"""
A Tkinter implementation of the classic `Simon` game
"""

from tkinter import Tk, Label, Button
from functools import partial
from typing import NamedTuple
import random

root = Tk()
root.title("Simon Game")


class Color(NamedTuple):
    name: str
    shade: str


COLORS: list[Color] = [
    Color("green", "#003300"),
    Color("red", "#550000"),
    Color("yellow", "#555500"),
    Color("blue", "#000055"),
]


class Simon:
    def __init__(self):
        self.score: int = 0
        self.timer_count: int = 0
        self.is_watching: int = True
        self.gameover: int = False
        self.game_state: list[int] = []
        self.temp_state: list[int] = []

        self.score_label = Label(root, text="0", font=("Courier", 25))
        self.score_label.grid(padx=10, pady=2, row=0, columnspan=2)

        self.how_to_label = Label(root, text="WATCH first, PLAY after")
        self.how_to_label.grid(padx=10, pady=2, row=1, columnspan=2)

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

    def change_color(self):
        for color in self.game_state:
            root.after(self.timer_count + 20, lambda: None)
            root.after(
                self.timer_count + 300,
                partial(self.buttons[color].config, bg=COLORS[color].name),
            )
            root.after(
                self.timer_count + 500,
                partial(self.buttons[color].config, bg=COLORS[color].shade),
            )

            self.timer_count += 220

    def press(self, button_index: int = 0):
        count = len(self.game_state)
        if count > 0 and not self.is_watching:
            self.temp_state.append(button_index)
            self.check(count - 1, button_index)
            count -= 1
        elif not self.gameover:
            self.score += 1
            self.score_label.config(text=self.score)
            self.is_watching = True
            self.temp_state.clear()
            self.first()

    def check(self, index: int = 0, button: int = 0):
        if self.game_state[index] != button:
            self.gameover = True
            self.how_to_label.configure(text="GAMEOVER")

    def first(self):
        if self.is_watching and not self.gameover:
            self.game_state.append(random.randint(0, 3))
            root.after(1000, self.change_color)
            self.is_watching = False


if __name__ == "__main__":
    Simon().first()
    root.mainloop()
