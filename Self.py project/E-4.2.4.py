print("\n")

print("i\'m glad to have you back Guys !\n today in my progrem i will make a date software!!\n")
print("Enter the date and the software will tell you What day is it in the week.\n")
import calendar

date = input("Enter the date as follows: dd/mm/yyyy\n\n print here:\t")

print()

day = int(date[:2])
month = int(date[3:5])
year = int(date[6:])

#print(year, month, day)

num_of_the_day = calendar.weekday(year, month, day)

name_of_the_day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

print("The day in the week is:",name_of_the_day[num_of_the_day], ".\n")

print("Thank you for taking part in my software !!\n")