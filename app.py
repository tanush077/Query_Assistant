import tkinter as tk
from tkinter import messagebox
from gui.main_window import create_main_window
from sql.database import execute_sql_query  

def submit_query():
    user_input = entry.get()
    try:
        result = execute_sql_query(user_input)
        messagebox.showinfo("Query Result", result)
    except Exception as e:
        messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    root.title("SQL Query App")

    label = tk.Label(root, text="Enter SQL Query:")
    label.pack()

    entry = tk.Entry(root)
    entry.pack()

    submit_button = tk.Button(root, text="Submit", command=submit_query)
    submit_button.pack()

    create_main_window(root) 

    root.mainloop()
