import calendar as cd

# Write a Python program to display calendar.
year = int(input("Enter the year : "))
month = int(input("Enter the month : "))
display = cd.month(year, month)
print(f"Calendar for year {year} and month {month} is displayed as {display}")
