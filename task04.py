from datetime import datetime, timedelta

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Jane Knox", "birthday": "1994.04.27"},
    {"name": "Marcelous Walles", "birthday": "1994.04.23"},
    {"name": "Bob Drill", "birthday": "1996.07.05"}
]

def get_upcoming_birthdays(users):
    current_date = datetime.today().date()
    congratulations = []

    for user in users:
        user["birthday"] = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = user["birthday"].replace(year=current_date.year)

        if birthday_this_year < current_date:
            continue

        if (birthday_this_year - current_date).days > 7:
            continue

        if birthday_this_year.weekday() == 5:
            congratulation_date = birthday_this_year + timedelta(days=2)
        elif birthday_this_year.weekday() == 6:
            congratulation_date = birthday_this_year + timedelta(days=1)
        else:
            congratulation_date = birthday_this_year

        congratulations.append({"name": user["name"], "congratulation_date": congratulation_date.strftime("%Y.%m.%d")})
        
    return congratulations

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на наступному тижні:", upcoming_birthdays)
