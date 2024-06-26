import tkinter as tk
from tkinter import simpledialog


marvel_data = []

with open('/Users/silacetinkaya/Desktop/marvel.txt', 'r') as file:

    next(file)
    for line in file:
        marvel_data.append(line.strip())

dropdown_values = list(set(entry.split()[0] for entry in marvel_data))

def update_text():
    selected_id = selected_id_var.get()
    textbox.delete(1.0, tk.END)  # Clear previous contents
    for entry in marvel_data:
        if entry.startswith(selected_id):
            textbox.insert(tk.END, entry + "\n")  # Insert new data

def add_entry():
    new_entry = simpledialog.askstring("Add Entry", "Enter ID MOVIE DATE MCU PHASE:")
    if new_entry:
        marvel_data.append(new_entry)
        update_text()

def list_all():
    textbox.delete(1.0, tk.END)  # Clear textbox
    for entry in marvel_data:
        textbox.insert(tk.END, entry + "\n")

root = tk.Tk()
root.title("Marvel Data")

# Dropdown list with IDs
selected_id_var = tk.StringVar(root)
selected_id_var.set(dropdown_values[0])  # Set default value
dropdown = tk.OptionMenu(root, selected_id_var, *dropdown_values)
dropdown.grid(row=0, column=0)

# Button to update textbox
update_button = tk.Button(root, text="Update Text", command=update_text)
update_button.grid(row=0, column=1)

# Button to add entry
add_button = tk.Button(root, text="Add", command=add_entry)
add_button.grid(row=0, column=2)

# Button to list all entries
list_button = tk.Button(root, text="LIST ALL", command=list_all)
list_button.grid(row=0, column=3)

# Textbox to display selected ID and entries
textbox = tk.Text(root, height=10, width=50)
textbox.grid(row=1, columnspan=4)

root.mainloop()
