def get_season(month):
    seasons = ('Winter', 'Spring', 'Summer', 'Autumn')
    month = (month - 1) % 12  # Adjust month to be 0-indexed

    if 0 <= month < 3:
        return seasons[0]
    elif 3 <= month < 6:
        return seasons[1]
    elif 6 <= month < 9:
        return seasons[2]
    else:
        return seasons[3]

while True:
    month = int(input("Enter a number of a month (1-12): "))

    if 1 <= month <= 12:
        season = get_season(month)
        print(f"The season for month {month} is {season}.")
    elif  month >= 12:
        print("Invalid input. Please enter a number between 1 and 12.")
    else:
        print("Invalid input. Please enter a valid number.")
