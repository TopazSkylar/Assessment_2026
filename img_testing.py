# Import module
from tkinter import *


# Create object
root = Tk()

# Adjust size
root.geometry("400x400")

# Add image file
bg = PhotoImage(file="album_r1.drawio.png")
bg2 = PhotoImage(file="album_r2.drawio.png")


# Create Canvas - where all the buttons and stuff will go
canvas1 = Canvas(root, width=400,
                 height=400)

canvas1.pack(fill="both", expand=True)

# Display image
canvas1.create_image(20, 100, image=bg,
                     anchor="w")
canvas1.create_image(200, 400, image=bg2, anchor="s")
# #ae23da
# backgrounds for title and instructions
canvas1.create_rectangle(396, 40, 10, 10, fill="#f0eaf3", outline="#ae23da")
canvas1.create_rectangle(2, 280, 396, 160, fill="#f0eaf3", outline="#ae23da")
# side borders
canvas1.create_rectangle(380, 700, 396, 10, fill="#ae23da", outline="#ae23da")
canvas1.create_rectangle(1, 700, 20, 10, fill="#ae23da", outline="#ae23da")

# Add Text
canvas1.create_text(200, 25, text="Taylor Swift Lyrics Quiz", font=("Satisfy",17), fill="#ae23da" )
canvas1.create_text(200, 200, text="You will be presented "
                                   "with the first lyrics from these 6 albums "
                                   "Try and guess em :))", width=300,
                    justify="center", font=("Balsamiq Sans", 12), fill="#ff14c7")

# Execute tkinter
root.mainloop()
