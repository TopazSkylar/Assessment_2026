# Import module
from tkinter import *
import tkinter as tk

# Create object
root = Tk()

# Adjust size
root.geometry("400x400")

# Add image file
bg = PhotoImage(file="album_r1.drawio.png")
bg2 = PhotoImage(file="album_r2.drawio.png")


# Create Canvas - where all the buttons and stuff will go
canvas_s = Canvas(root, width=400,
                  height=400)

canvas_s.pack(fill="both", expand=True)

# Display image
canvas_s.create_image(20, 100, image=bg,
                      anchor="w")
canvas_s.create_image(200, 400, image=bg2, anchor="s")
# #ae23da
# backgrounds for title and instructions
canvas_s.create_rectangle(396, 40, 10, 10, fill="#f0eaf3", outline="#f0eaf3")
canvas_s.create_rectangle(2, 280, 396, 160, fill="#f0eaf3", outline="#fc6ed5")
# side borders
# right
canvas_s.create_rectangle(380, 700, 396, 2, fill="#fc6ed5", outline="#fc6ed5")
# left
canvas_s.create_rectangle(1, 700, 20, 2, fill="#fc6ed5", outline="#fc6ed5")
# top slightly
canvas_s.create_rectangle(1, -10, 396, 5, fill="#fc6ed5", outline="#fc6ed5")

# Add Text
canvas_s.create_text(200, 25, text="Taylor Swift Lyrics Quiz", font=("Satisfy", 17), fill="#ae23da")
canvas_s.create_text(200, 200, text="You will be presented "
                                   "with the first lyrics from these 6 albums "
                                   "Try and guess em :))", width=300,
                     justify="center", font=("Bebas Neue", 15), fill="#ff14c7")

# where they enter the round number
entry = Entry(root)
entry_window = canvas_s.create_window(140, 250, anchor="nw", window=entry)

# add labels if they get it wrong
wrong_label = Label(root, text="Please enter an integer")
wrong_label.pack(pady=20)

def hide():
    wrong_label.pack_forget()


def show():
    wrong_label.pack()

# take the input and check it
def num_check():
    """Can only enter integers"""
    try:
        response = int(entry.get())
        if response <= 0:
            response = "<0/vE"
            return response
        else:
            print("You entered: ", response)
        return response
    except ValueError:
        response = "<0/vE"
        return response

 # displays error message
wrong_text = canvas_s.create_text(
    200, 240,
    text="Please enter a positive integer",
    font=("Permanent Marker", 8),
    fill="#FF0000",
    state="hidden"  # start hidden
)

# what the button does when you press it
def on_start():
    result = num_check()
    if result == "<0/vE":
        canvas_s.itemconfig(wrong_text, state="normal")
    else:
        canvas_s.itemconfig(wrong_text, state="hidden")
        print("Valid input:", result)



# Making the buttons - where they click the start button to check that it's a real int
button_s = tk.Button(root, text="start", anchor="nw", command=on_start, font=("Permanent Marker", 8))
button_s_window = canvas_s.create_window(270, 250, anchor="nw", window=button_s)


# Execute tkinter
root.title("Taylor Swift Lyrics Quiz")
root.mainloop()
