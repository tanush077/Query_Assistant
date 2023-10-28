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

def generate_query(user_input):

    base_query = "SELECT * FROM users WHERE"

    filters = user_input.split(",")

    conditions = []
    for filter_part in filters:
        key, value = filter_part.split(":")  # Assuming user input is in 'key: value' format
        key = key.strip()
        value = value.strip()

        if key == 'name':
            conditions.append(f" name = '{value}'")
        elif key == 'age':
            conditions.append(f" age = {value}")
        elif key == 'city':
            conditions.append(f" city = '{value}'")

    if conditions:
        query = f"{base_query} {' AND '.join(conditions)}"
        return query
    else:
        return "Invalid input. Please provide valid filters."

# Example user input
user_text_input = "name: John, age: 30, city: New York"

query = generate_query(user_text_input)
print(query)


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
