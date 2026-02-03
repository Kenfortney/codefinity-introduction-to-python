start_number = 5
countdown_values = []
final_value = 1

while final_value not in countdown_values:
    countdown_values.append(start_number)
    start_number -= 1

print("Discount countdown complete!")
print(countdown_values)