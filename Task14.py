def calculate_angle(hour, minute):
    # Normalize the hour value to a 12-hour format
    hour = hour % 12
    
    # Calculate the positions of the hour and minute hands in degrees
    hour_angle = (hour * 30) + (minute * 0.5)
    minute_angle = minute * 6
    
    # Calculate the difference between the two angles
    angle = abs(hour_angle - minute_angle)
    
    # The angle between the hands could be the smaller angle or its complement
    angle = min(angle, 360 - angle)
    
    return angle

# Get the time input from the user
hour = int(input("Enter the hour (0-23): "))
minute = int(input("Enter the minute (0-59): "))

# Calculate the angle
angle = calculate_angle(hour, minute)
print(f"The angle between the hour hand and minute hand is {angle} degrees.")
