import calendar

# print( calendar.TextCalendar(firstweekday=6).formatyear(2024))

m,d,y = input().split(" ")

day = calendar.weekday(int(y), int(m), int(d))
print((calendar.day_name[day]).upper())