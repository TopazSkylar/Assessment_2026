# # Import module
# from idlelib.browser import file_open
# from tkinter import *
# from venv import create
# import tkinter as tk
#
# def TestMath():
#     global result # to return calculation
#
#     result = int(entry.get())
#     result += 4
#
#     print(result)
#
# result = 0
#
# root = tk.Tk()
#
# entry = tk.Entry(root)
# entry.pack()
#
# button = tk.Button(root, text="Calculate", command=TestMath)
# button.pack()
#
# root.mainloop()
#
# import tkinter as tk
#
#
# class App:
#     def __init__(self, root):
#         self.root = root
#
#         # 1. Create the variable/widget
#         self.main_frame = tk.Frame(self.root, width=200, height=200, bg="blue")
#
#         # 2. Use pack to display it
#         self.main_frame.pack(pady=20)
#
#         # A button to trigger the change
#         self.btn = tk.Button(self.root, text="Change Color", command=self.change_style)
#         self.btn.pack()
#
#     def change_style(self):
#         # 3. Use .config() to change the frame's properties
#         self.main_frame.config(bg="red", relief="sunken", borderwidth=5)
#
#
# root = tk.Tk()
# app = App(root)
# root.mainloop()
#
# import tkinter as tk
#
# root = tk.Tk()
#
# # Create labels
# label1 = tk.Label(root, text="First Label", bg="red", fg="white")
# label2 = tk.Label(root, text="Second Label", bg="blue", fg="white")
#
# # Pack labels (default is side="top")
# label1.pack()
# label2.pack()
# label2.config(text = "a")
#
# root.mainloop()
# import csv
# import random
#
#
# def get_song_var():
#     """
#     From the csv
#     :return:
#     """
#
#
#     file = open("lyric_list.csv")
#     all_vars = list(csv.reader(file, delimiter=","))
#     file.close()
#
#     # remove the first row
#     all_vars.pop(0)
#
#     return all_vars
#
#
#
# def get_round_lyrics():
#
#     all_song_list = get_song_var()
#
#     round_song = []
#     dupe_check = []
#
#
#     # loop until we got them songs for each round
#     while len(round_song) < 4:
#         potential_song = random.choice(all_song_list)
#
#         # Get the songs and check it's not a duplicate
#         if potential_song[0] not in dupe_check:
#             round_song.append(potential_song)
#             dupe_check.append(potential_song[0])
#
#     print(f"List of songs, lyrics, album {round_song}")
#     print(f"List of songs chosen {dupe_check}")
#
#     # Randomly take the lyrics of all the generated songs and have it be the correct ans
#     potential_lyrics = []
#     potential_lyrics.extend([round_song[0][1], round_song[1][1], round_song[2][1], round_song[3][1]])
#     questioned_lyrics = random.choice(potential_lyrics)
#
#     print(f"questioned_lyrics =  {questioned_lyrics}")
#
# get_song_var()
# get_round_lyrics()

# Source - https://stackoverflow.com/a/42841266
# Posted by Bryan Oakley, modified by community. See post 'Timeline' for change history
# Retrieved 2026-05-01, License - CC BY-SA 3.0

# Source - https://stackoverflow.com/a/47860695
# Posted by Bryan Oakley
# Retrieved 2026-05-05, License - CC BY-SA 3.0

# import tkinter as tk
#
# root = tk.Tk()
# for text in (
#         "Hello", "short", "All the buttons are not the same size",
#         "Options", "Test2", "ABC", "This button is so much larger"):
#     button = tk.Button(root, text=text)
#     button.pack(side="top", fill="x")
#
# root.mainloop()

