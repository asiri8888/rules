import datetime
# get the current date and the time
now = datetime.datetime.now()
print(f"Current date time : {now}")

# Get only current date
today = datetime.date.today()
print(f"today is {today}")

#  Get only current time
current_time = now.time()
print(f"current time: {current_time}")



# date formatting
formatted_date_time = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"formatted date and time : {formatted_date_time}")

formatted_date = now.strftime("%A, %B %d, %Y")
print(f"formatted date  : {formatted_date}")


formatted_time = now.strftime("%I:%M %p") #12 hour format with Am/PM
print(f"formatted time: {formatted_time}")


# Add 7 days
future_date = now + datetime.timedelta(days=7)
print(f"7 days from now: {future_date}")


# substract 3 days
past_time = now - datetime.timedelta(hours=3)
print(f"time before 3 hours: {past_time}")


# calculate the different between 2 days
date1 = datetime.datetime(2024, 1, 1)
date2 = datetime.datetime(2025, 6,23)
difference = date2 - date1
print(f"Difference between days: {difference}")
print(f"Difference in days: {difference.days}")