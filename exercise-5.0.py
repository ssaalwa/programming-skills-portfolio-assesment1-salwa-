days_in_month = {
    1:31,
    2:28,
    3:31,
    4:30,
    5:31,
    6:30,
    7:31,
    8:31,
    9:30,
    10:31,
    11:30,
    12:31
}
month = int(input("enter the month number(1-12):" ))
if month in days_in_month:
    print(f"{days_in_month[month]}")
else:
    print("invalid month number.enter a number between 1 and 12.")