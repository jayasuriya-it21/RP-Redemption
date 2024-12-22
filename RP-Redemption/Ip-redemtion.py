def calculate_reward_points(subject_type, internal_marks, redemption_ratio):
    if subject_type == "normal":
        total_marks = 15
    elif subject_type == "lab":
        total_marks = 20
    else:
        print("Invalid subject type")
        return

    if subject_type == "normal":
        if internal_marks <= 8:
            points = internal_marks * redemption_ratio
        elif internal_marks <= 12:
            points = (internal_marks - 8) * redemption_ratio * 2 + 8 * redemption_ratio
        elif internal_marks <= 14:
            points = (internal_marks - 12) * redemption_ratio * 4 + 4 * redemption_ratio * 2 + 8 * redemption_ratio
        elif internal_marks <= 15:
            points = (internal_marks - 14) * redemption_ratio * 6 + 2 * redemption_ratio * 4 + 4 * redemption_ratio * 2 + 8 * redemption_ratio
        else:
            print("Invalid internal marks for normal subject")
            return
    elif subject_type == "lab":
        if internal_marks <= 10:
            points = internal_marks * redemption_ratio
        elif internal_marks <= 14:
            points = (internal_marks - 10) * redemption_ratio * 2 + 10 * redemption_ratio
        elif internal_marks <= 18:
            points = (internal_marks - 14) * redemption_ratio * 4 + 4 * redemption_ratio * 2 + 10 * redemption_ratio
        elif internal_marks <= 20:
            points = (internal_marks - 18) * redemption_ratio * 6 + 4 * redemption_ratio * 4 + 4 * redemption_ratio * 2 + 10 * redemption_ratio
        else:
            print("Invalid internal marks for lab subject")
            return
    else:
        print("Invalid internal marks")
        return

    return points

# Example usage:
redemption_ratio = int(input("Enter the redemption ratio for 1 Mark: "))  # You can change this based on your requirement
subject_type = input("Enter subject type (normal/lab): ").lower()
internal_marks = float(input("Enter internal marks: "))

reward_points = calculate_reward_points(subject_type, internal_marks, redemption_ratio)
if reward_points is not None:
    print(f"Reward points required: {reward_points}")
