def convert_to_24_hour(hour, minute, period):
    # Check if the period is "pm" and not noon
    if period == "pm" and hour != 12:
        hour += 12
    # Check if the period is "am" and it's midnight
    elif period == "am" and hour == 12:
        hour = 0

    # Format the hour and minute as a four-digit string
    hour_str = str(hour).zfill(2)
    minute_str = str(minute).zfill(2)

    # Concatenate the hour and minute strings
    time_24_hour = hour_str + minute_str

    return time_24_hour

hour = 8
minute = 30
period = "am"

result = convert_to_24_hour(hour, minute, period)
print(result)
