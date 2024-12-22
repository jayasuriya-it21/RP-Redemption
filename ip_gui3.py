import tkinter as tk
from tkinter import ttk

# Define the function to calculate the reward points
def calculate_reward_points():
    # Get the input values from the entries
    subject_type = subject_type_entry.get().lower()
    internal_marks = float(internal_marks_entry.get())
    redemption_ratio = int(redemption_ratio_entry.get())

    # Validate the input values
    if subject_type not in ["normal", "lab"]:
        result_label.config(text="Invalid subject type")
        return
    if internal_marks < 0 or internal_marks > 20:
        result_label.config(text="Invalid internal marks")
        return
    if redemption_ratio < 0:
        result_label.config(text="Invalid redemption ratio")
        return

    # Calculate the reward points based on the subject type and internal marks
    if subject_type == "normal":
        total_marks = 15
        if internal_marks <= 8:
            points = internal_marks * redemption_ratio
        elif internal_marks <= 12:
            points = (internal_marks - 8) * redemption_ratio * 2 + 8 * redemption_ratio
        elif internal_marks <= 14:
            points = (internal_marks - 12) * redemption_ratio * 4 + 4 * redemption_ratio * 2 + 8 * redemption_ratio
        elif internal_marks <= 15:
            points = (internal_marks - 14) * redemption_ratio * 6 + 2 * redemption_ratio * 4 + 4 * redemption_ratio * 2 + 8 * redemption_ratio
    elif subject_type == "lab":
        total_marks = 20
        if internal_marks <= 10:
            points = internal_marks * redemption_ratio
        elif internal_marks <= 14:
            points = (internal_marks - 10) * redemption_ratio * 2 + 10 * redemption_ratio
        elif internal_marks <= 18:
            points = (internal_marks - 14) * redemption_ratio * 4 + 4 * redemption_ratio * 2 + 10 * redemption_ratio
        elif internal_marks <= 20:
            points = (internal_marks - 18) * redemption_ratio * 6 + 4 * redemption_ratio * 4 + 4 * redemption_ratio * 2 + 10 * redemption_ratio

    # Display the result in the label
    result_label.config(text=f"Reward points required: {points}")

# Create the main window
window = tk.Tk()
window.title("Reward Points Calculator")
window.geometry("400x300")

# Create a frame to hold the widgets
frame = ttk.Frame(window, padding=10)
frame.pack()

# Create the labels and entries for the input values
subject_type_label = ttk.Label(frame, text="Enter subject type (normal/lab):")
subject_type_label.grid(row=0, column=0, sticky="w")
subject_type_entry = ttk.Entry(frame)
subject_type_entry.grid(row=0, column=1, sticky="w")

internal_marks_label = ttk.Label(frame, text="Enter internal marks:")
internal_marks_label.grid(row=1, column=0, sticky="w")
internal_marks_entry = ttk.Entry(frame)
internal_marks_entry.grid(row=1, column=1, sticky="w")

redemption_ratio_label = ttk.Label(frame, text="Enter the redemption ratio for 1 Mark:")
redemption_ratio_label.grid(row=2, column=0, sticky="w")
redemption_ratio_entry = ttk.Entry(frame)
redemption_ratio_entry.grid(row=2, column=1, sticky="w")

# Create a button to trigger the calculation
calculate_button = ttk.Button(frame, text="Calculate", command=calculate_reward_points)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

# Create a label to display the result
result_label = ttk.Label(frame, text="")
result_label.grid(row=4, column=0, columnspan=2)

# Enter the main event loop
window.mainloop()
