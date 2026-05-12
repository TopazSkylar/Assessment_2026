# Import module
import csv
import random

from tkinter import *
import tkinter as tk
import tkinter.font as tkFont

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

    # Randomly take the lyrics of all the generated songs and have it be the correct ans
    potential_lyrics = []
    # taken from all the chosen variable from the round_song
    potential_lyrics.extend([round_song[0][1], round_song[1][1], round_song[2][1], round_song[3][1]])
    # random
    questioned_lyrics = random.choice(potential_lyrics)
    # this will be the question
    print(f"questioned_lyrics =  {questioned_lyrics}")
    # takes the song name from the lyrics to note as the correct ans
    correct_index = potential_lyrics.index(questioned_lyrics)
    correct_song = final_round_song[correct_index]

    return questioned_lyrics, final_round_song, correct_song

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



        # as titled

        self.round_data = get_round_lyrics()
        self.choice = self.round_data[1]
        self.round_song = self.round_data[1]
        self.correct_choice = self.round_data[2]
        self.questioned_lyrics = self.round_data[0]
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

        self.button_hints = tk.Button(self.play_w, text="Hints", anchor="center", bg="#b2f7b7",  # Hints
                                 font=("Satisfy", 8), pady=10, padx=35)
        self.button_nr = tk.Button(self.play_w, text="Next Round", anchor="center", bg="#17c223",  # Next Round
                              font=("Satisfy", 8), pady=10, padx=35, command=self.new_round)
        self.button_stats = tk.Button(self.play_w, text="Stats", anchor="center", bg="#b2f7b7",  # Stats
                                 font=("Satisfy", 8), pady=10, padx=35)
        self.button_qg = tk.Button(self.play_w, text="Quit Game", anchor="center", bg="#b2f7b7",  # Quit Game
                              font=("Satisfy", 8), pady=8, padx=20,
                              command=self.end_game_button)

        # util buttons
        button_hints_w = self.canvas_p.create_window(30, 350, anchor="nw", window=self.button_hints)  # Hints
        button_nr_w = self.canvas_p.create_window(140, 300, anchor="nw", window=self.button_nr)  # New round
        button_stats_w = self.canvas_p.create_window(270, 350, anchor="nw", window=self.button_stats)  # stats
        button_qg_w = self.canvas_p.create_window(155, 350, anchor="nw", window=self.button_qg) # quit game


        # the title of rounds to show the user where they are
        self.heading_label = tk.StringVar()
        self.heading_label.set(f"Round {self.rounds_played.get()} out of {self.rounds_to_play.get()}")

        self.heading_text = self.canvas_p.create_text(200, 25, text=self.heading_label.get(), font=("Satisfy", 17), fill="#ae23da")

        # #ae23da
        self.funct()
        self.new_round()

    def funct(self):
        # below are how the question + question buttons are generated
        but_width_pixel = 120  # Define the width limit in pixels

        # lyrics
        self.lyrics_text = self.canvas_p.create_text(200, 100, text=self.questioned_lyrics, width=300,
                                  justify="center", font=("Bebas Neue", 15), fill="#11ad45")


        self.button_ans_1 = tk.Button(self.play_w, text=self.round_song[0], wraplength=but_width_pixel,
                                      command=lambda: self.check_ans(0))
        self.button_ans_2 = tk.Button(self.play_w, text=self.round_song[1], wraplength=but_width_pixel,
                                          command=lambda: self.check_ans(1))
        self.button_ans_3 = tk.Button(self.play_w, text=self.round_song[2], wraplength=but_width_pixel,
                                          command=lambda: self.check_ans(2))
        self.button_ans_4 = tk.Button(self.play_w, text=self.round_song[3], wraplength=but_width_pixel,
                                          command=lambda: self.check_ans(3))

        # check if they fit - adjust if not
        adjust_font(self.button_ans_1, self.round_song[0], but_width_pixel)
        adjust_font(self.button_ans_2, self.round_song[1], but_width_pixel)
        adjust_font(self.button_ans_3, self.round_song[2], but_width_pixel)
        adjust_font(self.button_ans_4, self.round_song[3], but_width_pixel)

        # How they select their answer
        button_ans_1_w = self.canvas_p.create_window(75, 210, anchor="nw", window=self.button_ans_1,
                                                         width=but_width_pixel)  # top left
        button_ans_2_w = self.canvas_p.create_window(210, 210, anchor="nw", window=self.button_ans_2,
                                                         width=but_width_pixel)  # top right
        button_ans_3_w = self.canvas_p.create_window(75, 260, anchor="nw", window=self.button_ans_3,
                                                         width=but_width_pixel)  # bottom left
        button_ans_4_w = self.canvas_p.create_window(210, 260, anchor="nw", window=self.button_ans_4,
                                                         width=but_width_pixel)  # bottom right

        self.update_round_display()

    def update_round_display(self):
        but_width_pixel = 120  # Define the width limit in pixels

        self.buttons = [
            self.button_ans_1,
            self.button_ans_2,
            self.button_ans_3,
            self.button_ans_4
        ]

        for i in range(4):
            self.buttons[i].config(text = self.round_song[i], state="normal")
            adjust_font(self.buttons[i], self.round_song[i], but_width_pixel)

            # update lyrics

            self.canvas_p.itemconfig(self.lyrics_text, text=self.questioned_lyrics)

            # update heading

            self.canvas_p.itemconfig(
                self.heading_text,
                text=f"Round {self.rounds_played.get()} of {self.rounds_to_play.get()}"
            )


    def new_round(self):
        """
        Chooses four song, picks one as the display lyrics Configures buttons
        with new ones
        """

        if self.rounds_played.get() == self.rounds_to_play.get():
            self.canvas_p.delete("result")
            self.canvas_p.create_text(200, 180, text=f"Score: {self.rounds_won.get()} / {self.rounds_to_play.get()}",
                    fill="blue", font=("Permanent Marker", 16), tags="result")

            return

        # retrieve number of rounds played, add one to it and configure heading
        rounds_played = self.rounds_played.get()
        rounds_played += 1
        self.rounds_played.set(rounds_played)

        rounds_to_play = self.rounds_to_play.get()



        # generates new data
        self.round_data = get_round_lyrics()
        self.choice = self.round_data[1]
        self.round_song = self.round_data[1]
        self.correct_choice = self.round_data[2]
        self.questioned_lyrics = self.round_data[0]

        # clears it
        self.canvas_p.delete("result")

        # update widgets
        self.update_round_display()

        self.button_nr.config(state="disabled")

    def check_ans(self, idx):

        selected = self.choice[idx]

        # remove old result
        self.canvas_p.delete("result")


        if selected == self.correct_choice:
            result_text = f"Success! {selected} is correct"
            result_color = "green"
            self.rounds_won.set(self.rounds_won.get() + 1)

        else:
            result_text = f"Oops! It was {self.correct_choice}"
            result_color = "red"

        self.canvas_p.create_text(200, 180, text=result_text, fill=result_color, font=("Arial", 12), tags="result")

        for item in self.buttons:
            item.config(state="disabled")
        self.button_nr.config(state="normal")

# Execute tkinter
root.title("Taylor Swift Lyrics Quiz")

root.mainloop()





