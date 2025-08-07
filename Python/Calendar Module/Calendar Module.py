
import calendar

date = list(map(int,input().split()))
month = date[0]
day = date[1]
year = date[2]

days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]

day_number = calendar.weekday(year, month, day)

print(days[day_number])


