#FutureTime.py
#Name:Bennett Schulte
#Date:9/1/2025
#Assignment:Lab 2

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = now.hour - 5
  currentMinute = now.minute

 

  #TODO:
  #Ask user for hours
  addHours = int(input("Please enter the number of hours to add:  "))
  #Ask user for minutes
  addMinute = int(input("Please enter the number of minutes to add:  "))
  #Calculate the time after the user-supplied time has passed.
  totalMinutes = currentMinute + addMinute
  extraHours = totalMinutes // 60
  finalMinutes = totalMinutes % 60

  totalHours = currentHour + addHours +extraHours
  finalHours = totalHours % 24

  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"
  print("Future time:", finalHours, ":", finalMinutes)

if __name__ == '__main__':
  main()
