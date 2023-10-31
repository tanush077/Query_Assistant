import tkinter as tk
from tkinter import messagebox
from sql.database import execute_sql_query  # Path to be adjusted
import os

def submit_query():
    user_input = entry.get()
    try:
        result = execute_sql_query(user_input)
        messagebox.showinfo("Query Result", result)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def clear_text():
    entry.delete(0, "end")  # Clear the text in the entry widget

# Create the Tkinter window
root = tk.Tk()
root.title("SQL Query App")

# Set the window resolution
window_width = 1000
window_height = 600

# Calculate the position to center the window
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Set the background color of the window to black (default dark mode)
root.configure(bg="black")

# Create a frame to center the elements with a black background
frame = tk.Frame(root, bg="black")
frame.pack(expand=True)

# Create a function to toggle the mode
def toggle_mode():
    current_mode[0] = 1 - current_mode[0]
    update_mode()

# Create a function to update the UI based on the mode
def update_mode():
    if current_mode[0] == 0:
        # Dark Mode
        root.configure(bg="black")
        label.config(bg="black", fg="white")
        entry.config(bg="black", fg="white")
        submit_button.config(bg="#61A3BA", fg="white")
        clear_button.config(bg="#61A3BA", fg="white")
        toggle_button.config(image=night_mode_img)
        toggle_button.config(command=toggle_mode)
        label.config(text="Dark Mode is On")
    else:
        # Light Mode
        root.configure(bg="white")
        label.config(bg="white", fg="black")
        entry.config(bg="white", fg="black")
        submit_button.config(bg="lightblue", fg="black")
        clear_button.config(bg="lightblue", fg="black")
        toggle_button.config(image=day_mode_img)
        toggle_button.config(command=toggle_mode)
        label.config(text="Light Mode is On")

# Create widgets and center them using the grid geometry manager
label = tk.Label(frame, text="Enter SQL Query:", bg="black", fg="white", font=("Helvetica", 16))
label.grid(row=0, column=0, columnspan=2, pady=20)

entry = tk.Entry(frame, bg="black", fg="white", font=("Helvetica", 14))
entry.grid(row=1, column=0, columnspan=2, padx=20, pady=20, ipadx=20)

submit_button = tk.Button(frame, text="Submit", command=submit_query, bg="#61A3BA", fg="white", font=("Helvetica", 14))
clear_button = tk.Button(frame, text="Clear", command=clear_text, bg="#61A3BA", fg="white", font=("Helvetica", 14))

submit_button.grid(row=2, column=0, padx=10, pady=20, ipadx=20)
clear_button.grid(row=2, column=1, padx=10, pady=20, ipadx=20)

# Load the images for the toggle button
assets_path = os.path.join(os.getcwd(), "assets")  # Path to the assets folder in the main directory
night_mode_img = tk.PhotoImage(file=os.path.join(assets_path, "on.png"))
day_mode_img = tk.PhotoImage(file=os.path.join(assets_path, "off.png"))

# Create the toggle button
toggle_button = tk.Button(root, image=night_mode_img, bd=0, command=toggle_mode)
toggle_button.pack(pady=20)

# Initialize the UI in "Dark Mode" and keep the label text always visible
current_mode = [0]
update_mode()

root.mainloop()
