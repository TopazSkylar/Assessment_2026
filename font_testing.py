import tkinter as tk
from tkextrafont import Font

# 1. Initialize Tkinter
root = tk.Tk()
root.geometry("300x200")

label = tk.Label(root, text="Hello Custom Font!", font=("Satisfy", 20))
label.pack(pady=2)
label_2 = tk.Label(root, text="Hello Custom Font!", font=("Balsamiq Sans", 20))
label_2.pack(pady=5)
label_3 = tk.Label(root, text="Hello Custom Font!", font=("Permanent Marker", 20))
label_3.pack(pady=4)


root.mainloop()
