from datetime import datetime, timedelta

given_date = datetime(2020, 2, 25)
print("given date")
print(given_date)

days_to_subtract =7
ans_date = given_date - timedelta(days=days_to_subtract)
print("newdate")
print(ans_date)

