start_number = 5
countdown_values = []

while start_number > 0:
    print(f"Countdown in progress: {start_number} remaining")
    countdown_values.append(start_number)
    start_number -= 1


print("Discount countdown complete!")
print(f"Countdown updated: {countdown_values} remain")