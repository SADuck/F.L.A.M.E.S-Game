import tkinter as tk
from tkinter import messagebox

def calculate_relationship(name1, name2):
    # Remove common characters
    name1_set = set(name1.lower())
    name2_set = set(name2.lower())
    common_chars = name1_set.intersection(name2_set)
    unique_chars = (name1_set - common_chars) | (name2_set - common_chars)

    # Calculate the total number of unique letters
    total_letters = len(unique_chars)

    # FLAMES algorithm
    flames = ["Friends", "Lovers", "Affectionate", "Married", "Enemies", "Siblings"]
    result_index = (total_letters % len(flames)) - 1

    return flames[result_index]

def check_relationship():
    name1 = entry_name1.get()
    name2 = entry_name2.get()

    if name1 and name2:
        result = calculate_relationship(name1, name2)
        messagebox.showinfo("Result", f"The relationship is: {result}")
    else:
        messagebox.showwarning("Error", "Please enter both names.")

# Create the main window
root = tk.Tk()
root.title("F.L.A.M.E.S. Game")

# Labels and entry fields
label_name1 = tk.Label(root, text="Enter Name 1:")
entry_name1 = tk.Entry(root)
label_name2 = tk.Label(root, text="Enter Name 2:")
entry_name2 = tk.Entry(root)

# Button to calculate relationship
button_calculate = tk.Button(root, text="Calculate Relationship", command=check_relationship)

# Grid layout
label_name1.grid(row=0, column=0)
entry_name1.grid(row=0, column=1)
label_name2.grid(row=1, column=0)
entry_name2.grid(row=1, column=1)
button_calculate.grid(row=2, columnspan=2)

root.mainloop()
