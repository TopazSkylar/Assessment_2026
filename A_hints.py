# Import module
import csv
import random

from tkinter import *
import tkinter as tk
import tkinter.font as tkFont
from functools import partial  # to prevent unwanted windows

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


def get_song_var():
    """
    From the csv
    :return:
    """

    file = open("lyric_list.csv")
    all_vars = list(csv.reader(file, delimiter=","))
    file.close()

    # remove the first row
    all_vars.pop(0)

    return all_vars


def get_round_lyrics():
    # grab all the info from the csv
    all_song_list = get_song_var()

    round_song = []
    final_round_song = []
    potential_lyrics = []

    # loop until we got them songs for each round
    while len(round_song) < 4:
        potential_song = random.choice(all_song_list)

        # Get the songs and check it's not a duplicate
        if potential_song[0] not in final_round_song:
            round_song.append(potential_song)
            final_round_song.append(potential_song[0])
    # everything
    print(f"List of songs, lyrics, album {round_song}")
    # final
    print(f"List of songs chosen {final_round_song}")

    # takes rand song from select
    questioned_song = random.choice(round_song)
    questioned_lyrics = questioned_song[1]  # Take the lyrics of all the song and have it be the thing user sees
    album = questioned_song[2]  # The album

    # FIXED: Find the correct song name directly from the picked questioned_song object
    correct_song = questioned_song[0]

    return questioned_lyrics, final_round_song, correct_song, album


def adjust_font(button, text, max_width):
    """have max_width, shrink until it's within it """
    current_size = 8  # assume this much at start
    test_font = tkFont.Font(family="Permanent Marker", size=current_size)

    # Decrease size until it fits
    while test_font.measure(text) > max_width and current_size > 6:  # 6 is the minimum readability
        current_size -= 1
        test_font.configure(size=current_size)

    button.configure(font=("Permanent Marker", current_size))


class Play:
    # Adjust size

    def __init__(self, result):
        # as titled

        self.round_data = get_round_lyrics()
        self.choice = self.round_data[1]
        self.round_song = self.round_data[1]
        self.correct_choice = self.round_data[2]
        self.questioned_lyrics = self.round_data[0]
        # self.album = int(self.round_data[3])

        # texting purposes
        # self.album = 1
        # self.album = 2
        # self.album = 3
        # self.album = 4
        # self.album = 5
        self.album = 6

        self.rounds_played = IntVar()
        self.rounds_played.set(0)
        self.rounds_to_play = IntVar()
        self.rounds_to_play.set(result)
        self.rounds_to_play.set(result)
        self.rounds_won = IntVar()
        # lyric list per round

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

        self.button_hints = tk.Button(self.play_w, text="Hints", anchor="center", bg="#b2f7b7",  # Hints
                                      font=("Satisfy", 8), pady=10, padx=35, command=self.to_hints)

        # util buttons
        button_hints_w = self.canvas_p.create_window(30, 350, anchor="nw", window=self.button_hints)  # Hints


    def to_hints(self):
        """
        Displays hints for playing game
        :return:
        """
        # disable help button
        current_album = self.album
        self.button_hints.config(state="disabled")
        DisplayHints(self, current_album)


class DisplayHints:

    def __init__(self, partner, current_album):

        # preset variables before generating anything
        if current_album == 1:
            hbtxt = "Taylor Swift"
            bgf = "hints_bg_1.png"
            bg = "#029c67"
        elif current_album == 2:
            hbtxt = "Fearless"
            bgf = "hints_bg_2.png"
            bg = "#e9c581"
        elif current_album == 3:
            hbtxt = "Speak Now"
            bgf = "hints_bg_3.png"
            bg = "#a3277b"
        elif current_album == 4:
            hbtxt = "Red"
            bgf = "hints_bg_4.png"
            bg = "#a12f49"
        elif current_album == 5:
            hbtxt = "1989"
            bgf = "hints_bg_5.png"
            bg = "#0bc0d4"
        else:
            hbtxt = "Reputation"
            bgf = "hints_bg_6.png"
            bg = "#c5c5c5"

        self.bg_color = bg

        self.hints = Toplevel()
        # Create Canvas - where all the buttons and stuff will go
        self.canvas_h = Canvas(self.hints, width=400,
                               height=400, bg = self.bg_color)

        # Adjust size
        self.hints.geometry("400x400")
        self.hints.title("Taylor Swift Lyrics Quiz Play")
        self.canvas_h.pack(fill="both", expand=True)

        self.bg_h = PhotoImage(file = bgf)
        print(self.bg_h)

        # when cycling through img options, need to keep a constant in order to display the img
        self.canvas_h.image = self.bg_h

        self.canvas_h.create_image(200, 200, image=self.bg_h)


        # text used for hints
        self.head_s_disp = self.canvas_h.create_text(200, 12, text="Hints", width=300,
                                                     justify="left", font=("Permanent Marker", 22, "bold"),
                                                     fill="#000000")
        self.hint_disp = self.canvas_h.create_text(200, 37, text=f"This is from {hbtxt}",
                                                   font=("Bebas Neue", 18, "bold"))

        self.dismiss_button = tk.Button(self.hints,
                                      font=("Permanent Marker", 12, "bold"),
                                      text="Dismiss", bg="#D4D5CD",
                                         fg="#444959", width=7,
                                         command=partial(self.close_hints, partner))

        button_dismiss_button = self.canvas_h.create_window(160, 355, anchor="nw", window=self.dismiss_button)  # disp dismiss




    def close_hints(self, partner):
        """
        Closes hints dialogue box (and enables hints button)
        """
        # Put hints button back to normal...
        partner.button_hints.config(state="normal")
        self.hints.destroy()


# main routine
# Execute tkinter
root.title("Taylor Swift Lyrics Quiz")

root.mainloop()
