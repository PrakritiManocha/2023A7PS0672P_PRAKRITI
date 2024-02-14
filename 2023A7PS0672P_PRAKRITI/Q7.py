def calculate_angle(time):
    hours, minutes = map(int, time.split(':'))
    angle_diff=(30*hours)-((11/2)*minutes)
    return min(angle_diff, 360 - angle_diff)


time=input("Enter time:")
angle = calculate_angle(time)
print("The angle between the hour and minute hands for the time is",angle)
