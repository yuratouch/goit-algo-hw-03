from datetime import datetime, timedelta

input_date = input("Please enter date in format yyyy-mm-dd >>> ")

def get_days_from_today(date:str):
    try:
        given_date = datetime.strptime(date, "%Y-%m-%d")
        current_date = datetime.now()
        diff = current_date - given_date
        res = diff.days
        return res
    except ValueError:
        print("Date is not valid!")

print(get_days_from_today(input_date))