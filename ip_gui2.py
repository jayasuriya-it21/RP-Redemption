import tkinter as tk
from tkinter import ttk

def calculate_reward_points(*args):
    subject_type = subject_type_var.get().lower()
    try:
        internal_marks = float(internal_marks_var.get())
        redemption_ratio = int(redemption_ratio_var.get())

        if subject_type in ["normal", "lab"] and 0 <= internal_marks <= 20:
            result = f"Reward points required: {calculate_reward_points_function(subject_type, internal_marks, redemption_ratio)}"
        else:
            result = "Invalid input"
    except ValueError:
        result = "Invalid input"

    result_label.config(text=result)

def calculate_reward_points_function(subject_type, internal_marks, redemption_ratio):
    total_marks = 15 if subject_type == "normal" else 20

    if subject_type == "normal":
        if internal_marks <= 8:
            points = internal_marks * redemption_ratio
        elif internal_marks <= 12:
            points = (internal_marks - 8) * redemption_ratio * 2 + 8 * redemption_ratio
        elif internal_marks <= 14:
            points = (internal_marks - 12) * redemption_ratio * 4 + 4 * redemption_ratio * 2 + 8 * redemption_ratio
        elif internal_marks <= 15:
            points = (internal_marks - 14) * redemption_ratio * 6 + 2 * redemption_ratio * 4 + 4 * redemption_ratio * 2 + 8 * redemption_ratio
    elif subject_type == "lab":
        if internal_marks <= 10:
            points = internal_marks * redemption_ratio
        elif internal_marks <= 14:
            points = (internal_marks - 10) * redemption_ratio * 2 + 10 * redemption_ratio
        elif internal_marks <= 18:
            points = (internal_marks - 14) * redemption_ratio * 4 + 4 * redemption_ratio * 2 + 10 * redemption_ratio
        elif internal_marks <= 20:
            points = (internal_marks - 18) * redemption_ratio * 6 + 4 * redemption_ratio * 4 + 4 * redemption_ratio * 2 + 10 * redemption_ratio

    return points

# Create the main window
root = tk.Tk()
root.title("Reward Points Calculator")

# Create variables for live updates
subject_type_var = tk.StringVar()
internal_marks_var = tk.StringVar()
redemption_ratio_var = tk.StringVar()

# Callback function to calculate reward points on live changes
subject_type_var.trace_add("write", calculate_reward_points)
internal_marks_var.trace_add("write", calculate_reward_points)
redemption_ratio_var.trace_add("write", calculate_reward_points)

# Create and place widgets
subject_type_label = tk.Label(root, text="Subject Type:")
subject_type_combobox = ttk.Combobox(root, textvariable=subject_type_var, values=["Normal", "Lab"])
subject_type_combobox.set("Normal")

internal_marks_label = tk.Label(root, text="Internal Marks:")
internal_marks_entry = tk.Entry(root, textvariable=internal_marks_var)

redemption_ratio_label = tk.Label(root, text="Redemption Ratio for 1 Mark:")
redemption_ratio_entry = tk.Entry(root, textvariable=redemption_ratio_var)

result_label = tk.Label(root, text="Result: ")

# Grid layout
subject_type_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
subject_type_combobox.grid(row=0, column=1, padx=5, pady=5, sticky="w")

internal_marks_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
internal_marks_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

redemption_ratio_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
redemption_ratio_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

result_label.grid(row=3, column=0, columnspan=2, pady=5)

# Start the GUI main loop
root.mainloop()
