""" LISTBOX"""
import tkinter as tk

root = tk.Tk()
root.title("ELECTRONIC GADGETS")

# Create a listbox
listbox = tk.Listbox(root, bg="white", fg="black", width=40, height=10)
listbox.pack(padx=10, pady=10)

# Add items to the listbox
listbox.insert(1, "PHONE")
listbox.insert(2, "LAPTOP")
listbox.insert(3, "EARBUDS")
listbox.insert(4, "HEADPHONES")
listbox.insert(5, "JOYPAD")

root.mainloop()

"""" SCROLLBAR"""
import tkinter as tk

root = tk.Tk()
root.title("Scrollbar ELECTRONIC GADGETS")

# Create a listbox
listbox = tk.Listbox(root, bg="white", fg="black", width=40, height=10)
listbox.pack(padx=10, pady=10)

# Create a scrollbar
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Configure the listbox with the scrollbar
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Add items to the listbox
listbox.insert(1, "PHONE")
listbox.insert(2, "LAPTOP")
listbox.insert(3, "EARBUDS")
listbox.insert(4, "HEADPHONES")
listbox.insert(5, "JOYPAD")
listbox.insert(6, "WATCH")
listbox.insert(7, "CHARGER")
listbox.insert(8, "HARDDRIVE")
listbox.insert(9, "EARPHONES")
listbox.insert(10, "DESKTOP")
listbox.insert(11, "MONITOR")
listbox.insert(12, "SPEAKERS")
listbox.insert(13, "POWER BANK")
listbox.insert(14, "ROUTER")
listbox.insert(15, "MIFI")
listbox.insert(16, "PLAYSTATION 5")
listbox.insert(17, "TABLET")
listbox.insert(18, "IPHONE")
listbox.insert(19, "TV")
listbox.insert(20, "CABLES")
listbox.insert(21, "ADAPTOR")
listbox.insert(22, "MIC")
listbox.insert(23, "SSD")
listbox.insert(24, "RAM")
listbox.insert(25, "BATTERY")

root.mainloop()


""" MENU """
import tkinter as tk

root = tk.Tk()
root.title("Menu Example")

# Create a menu
menu = tk.Menu(root)

# Create a file menu
file_menu = tk.Menu(menu, tearoff=0)
file_menu.add_command(label="New", command=lambda: print("New"))
file_menu.add_command(label="Open", command=lambda: print("Open"))
file_menu.add_command(label="Save", command=lambda: print("Save"))
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Add the file menu to the main menu
menu.add_cascade(label="File", menu=file_menu)

# Add the menu to the root window
root.config(menu=menu)

root.mainloop()


""" CANVAS """

import tkinter as tk

root = tk.Tk()
root.title("Canvas Example")

# Create a canvas
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack(padx=10, pady=10)

# Create a frame inside the canvas
frame = tk.Frame(canvas)
canvas.create_window(0, 0, window=frame, anchor=tk.NW)

# Add widgets to the frame
for i in range(10):
    label = tk.Label(frame, text=f"Label {i+1}")
    label.pack(padx=5, pady=5)

# Configure the canvas to scroll
canvas.configure(scrollregion=canvas.bbox(tk.ALL))

root.mainloop()
