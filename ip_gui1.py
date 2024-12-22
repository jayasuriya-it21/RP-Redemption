import tkinter as tk
from tkinter import ttk

def calculate_reward_points():
    subject_type = subject_type_var.get().lower()
    internal_marks = float(internal_marks_entry.get())
    redemption_ratio = int(redemption_ratio_entry.get())

    result = "Invalid input"

    if subject_type in ["normal", "lab"] and 0 <= internal_marks <= 20:
        result = f"Reward points required: {calculate_reward_points_function(subject_type, internal_marks, redemption_ratio)}"

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

# Create and place widgets
subject_type_label = tk.Label(root, text="Subject Type:")
subject_type_var = tk.StringVar()
subject_type_combobox = ttk.Combobox(root, textvariable=subject_type_var, values=["Normal", "Lab"])
subject_type_combobox.set("Normal")

internal_marks_label = tk.Label(root, text="Internal Marks:")
internal_marks_entry = tk.Entry(root)

redemption_ratio_label = tk.Label(root, text="Redemption Ratio for 1 Mark:")
redemption_ratio_entry = tk.Entry(root)

calculate_button = tk.Button(root, text="Calculate Reward Points", command=calculate_reward_points)

result_label = tk.Label(root, text="Result: ")

# Grid layout
subject_type_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
subject_type_combobox.grid(row=0, column=1, padx=5, pady=5, sticky="w")

internal_marks_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
internal_marks_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

redemption_ratio_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
redemption_ratio_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

result_label.grid(row=4, column=0, columnspan=2, pady=5)

# Start the GUI main loop
root.mainloop()
