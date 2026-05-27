# Import module
import csv
import random

from tkinter import *
import tkinter as tk
import tkinter.font as tkFont
from functools import partial # to prevent unwanted windows


# Create object
root = Tk()
# Create Canvas - where all the buttons and stuff will go
canvas2 = Canvas(root, width=400,
                 height=400)

canvas2.pack(fill="both", expand=True)

# Adjust size
root.geometry("400x400")
def on_start():
    Play(5)

    root.withdraw()

# Making the buttons - where they click the start button to check that it's a real int
button_s = tk.Button(root, text="start", anchor="nw", command=on_start, font=("Permanent Marker", 8))
button_s_window = canvas2.create_window(270, 250, anchor="nw", window=button_s)



def adjust_font(button, text, max_width):
    """have max_width, shrink until it's within it """
    current_size = 8 # assume this much at start
    test_font = tkFont.Font(family="Permanent Marker", size=current_size)

    # Decrease size until it fits
    while test_font.measure(text) > max_width and current_size > 6: # 6 is the minimum readability
        current_size -= 1
        test_font.configure(size=current_size)

    button.configure(font=("Permanent Marker", current_size))


class Play:
    # Adjust size


    def __init__(self, result):

        # testing parameters
        # self.rounds_played = 5
        # self.rounds_played = 11
        self.rounds_played = 101

        # testing parameters
        # self.rounds_won = 5
        # self.rounds_won = 5
        self.rounds_won = random.randint(1,100)


        # Create object
        self.play_w = Toplevel()
        # Adjust size
        self.play_w.geometry("400x400")
        self.play_w.title("Taylor Swift Lyrics Quiz Play")
        # destroy window when end game is pressed
        self.end_game_button = self.play_w.destroy

        # Create Canvas - where all the buttons and stuff will go
        self.canvas_p = Canvas(self.play_w, width=400,
                               height=400)

        self.canvas_p.pack(fill="both", expand=True)

        # backgrounds for title and instructions
        self.canvas_p.create_rectangle(360, 200, 40, 50, outline="#fc6ed5")
        # side borders
        # right
        self.canvas_p.create_rectangle(380, 700, 396, 2, fill="#fc6ed5", outline="#fc6ed5")
        # left
        self.canvas_p.create_rectangle(1, 700, 20, 2, fill="#fc6ed5", outline="#fc6ed5")
        # top slightly
        self.canvas_p.create_rectangle(1, -10, 396, 5, fill="#fc6ed5", outline="#fc6ed5")

        # half the screen in pink - check if centered
        self.canvas_p.create_rectangle(200, 400, 396, 2, fill="#fc6ed5", outline="#fc6ed5")

        self.button_stats = tk.Button(self.play_w, text="Stats", anchor="center", bg="#b2f7b7",  # Stats
                                 font=("Satisfy", 8), pady=10, padx=35, command=self.to_stats)

        button_stats_w = self.canvas_p.create_window(270, 350, anchor="nw", window=self.button_stats)  # stats


    def to_stats(self):
        # grabs all the info that the stats display will need
        # normally has self.rounds_played.get() as it updates
        rounds_played = self.rounds_played
        # normally has self.rounds_won.get() as it updates
        rounds_won = self.rounds_won
        bundle = [rounds_played,rounds_won]
        # self.button_stats.config(state="disabled")

        Stats(self, bundle)



class Stats:
    """
    Displays stats for Color Quest Game
    """

    def __init__(self, partner, bundle):

        # Create object
        self.stats = Toplevel()
        # Adjust size
        self.stats.geometry("400x400")
        self.stats.title("Taylor Swift Lyrics Quiz Play")
        # destroy window when end game is pressed
        self.dismiss_button = self.stats.destroy

        # Create Canvas - where all the buttons and stuff will go
        self.canvas_s = Canvas(self.stats, width=400,
                               height=400)

        self.canvas_s.pack(fill="both", expand=True)

        # img for bg
        self.bg_s = PhotoImage(file="stats_bg.drawio.png")

        self.canvas_s.create_image(200,200, image=self.bg_s)

        # Extract information from master list...
        rounds_played = bundle[0]
        rounds_won = bundle[1]

        # If users press cross at top, closes help and
        # 'releases' help button
        self.stats.protocol('WM_DELETE_WINDOW',
                                   partial(self.close_stats, partner))

        # Math to populate Stats dialogue
        success_rate = round(rounds_won / rounds_played * 101,1)

        # Strings for Stats Labels...
        success_string = f"Success Rate: {rounds_won} / {rounds_played}"

        self.head_s_disp = self.canvas_s.create_text(115, 100, text="Statistics", width=300,
                                  justify="left", font=("Permanent Marker", 24, "bold"), fill="#3B4053")
        self.round_disp = self.canvas_s.create_text(135, 180, text=success_string, width=300,
                                                    justify="left",  font=("Permanent Marker", 15, "bold"), fill="#444959")
        self.round_disp = self.canvas_s.create_text(175, 260, text=f"Percentage correct = {success_rate}", width=300,
                                                    justify="left", font=("Permanent Marker", 15, "bold"), fill="#383C47")

        self.dismiss_button = tk.Button(self.stats,
                                      font=("Permanent Marker", 12, "bold"),
                                      text="Dismiss", bg="#D4D5CD",
                                         fg="#444959", width=7,
                                         command=partial(self.close_stats, partner))

        button_dismiss_button = self.canvas_s.create_window(160, 340, anchor="nw", window=self.dismiss_button)  # disp dismiss

    # closes help dialogue (by button and x at the top of dialogue)

    def close_stats(self, partner):
            """
            Closes stats dialogue box (and enables stats button)
            """
            # Put stats button back to normal...
            partner.button_stats.config(state="normal")
            self.stats.destroy()


# Execute tkinter
root.title("Taylor Swift Lyrics Quiz")

root.mainloop()





