import tkinter as tk

root = tk.Tk()
####clickable Button

def button_click():
    print("Button clicked!")

# Create a Button widget
button = tk.Button(root, text="Click me", command=button_click)
button.pack()

root.mainloop()

######FRAME 
import tkinter as tk

root = tk.Tk()
root.title("Frame Example")

# Create a Frame
frame = tk.Frame(root, bg="lightgray", padx=10, pady=10)
frame.pack()

# Add widgets to the Frame
label = tk.Label(frame, text="Label inside Frame")
label.pack()

button = tk.Button(frame, text="Button inside Frame")
button.pack()

root.mainloop()


##### ENTRY WIDGET
import tkinter as tk

root = tk.Tk()
root.title("Entry Practice")
# Create an Entry widget
entry = tk.Entry(root)
entry.pack()

# Define a function to handle the entry submission
def submit_entry():
    user_input = entry.get()
    print(f"You entered: {user_input}")
    entry.delete(0, tk.END)  # Clear the entry field

# Create a button to submit the entry
submit_button = tk.Button(root, text="Submit", command=submit_entry)
submit_button.pack()

root.mainloop()


####CHECKBUTTON WIDGET
import tkinter as tk

root = tk.Tk()
root.title("Checkbutton Practice")

# Create a BooleanVar to store the checkbox state
checked = tk.BooleanVar()

# Define a function to handle the checkbox state change
def show_state():
    if checked.get():
        print("Checkbox is checked")
    else:
        print("Checkbox is unchecked")

# Create the Checkbutton
check_button = tk.Checkbutton(root, text="Check me", variable=checked, command=show_state)
check_button.pack()

root.mainloop()


######Radiobutton WIDGET
import tkinter as tk

root = tk.Tk()
root.title("Radiobutton Practice")

# Create a StringVar to store the selected value
selected_value = tk.StringVar()

# Create the Radiobuttons
radio_button_1 = tk.Radiobutton(root, text="Option 1", value="option1", variable=selected_value)
radio_button_2 = tk.Radiobutton(root, text="Option 2", value="option2", variable=selected_value)
radio_button_3 = tk.Radiobutton(root, text="Option 3", value="option3", variable=selected_value)

# Pack the Radiobuttons
radio_button_1.pack()
radio_button_2.pack()
radio_button_3.pack()

root.mainloop()