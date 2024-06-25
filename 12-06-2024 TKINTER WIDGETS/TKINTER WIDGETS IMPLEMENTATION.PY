import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Tkinter Widget PRACTICE BY SCHOLAR")

# Frame widget
frame = ttk.Frame(root, padding=10)
frame= tk.Frame(root,bg="Green")
frame.grid()

# Label widget
label = ttk.Label(frame, text="Enter your name:")
label.grid(row=0, column=0)

# Entry widget
name_entry = ttk.Entry(frame)
name_entry.grid(row=0, column=1)

# Button widget
def greet():
    name = name_entry.get()
    greeting_label.config(text=f"Hello, {name}!")

greet_button = ttk.Button(frame, text="Greet", command=greet)
greet_button.grid(row=1, column=1)

# Checkbutton widget
is_student = tk.BooleanVar()
checkbutton = ttk.Checkbutton(frame, text="Are you a student?", variable=is_student)
checkbutton.grid(row=2, column=0, columnspan=2)

# Radiobutton widgets
gender = tk.StringVar()
radio_frame = ttk.Frame(frame)
radio_frame.grid(row=3, column=0, columnspan=2)

male_radio = ttk.Radiobutton(radio_frame, text="Male", variable=gender, value="male")
male_radio.grid(row=0, column=0)

female_radio = ttk.Radiobutton(radio_frame, text="Female", variable=gender, value="female")
female_radio.grid(row=0, column=1)

other_radio = ttk.Radiobutton(radio_frame, text="Other", variable=gender, value="other")
other_radio.grid(row=0, column=2)

# Label widget for greeting
greeting_label = ttk.Label(frame, text="")
greeting_label.grid(row=4, column=0, columnspan=2)

root.mainloop()