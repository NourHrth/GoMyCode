import time
import datetime
 
def countdown(m, s):
    total_seconds = m * 60 + s
    while total_seconds > 0:
        timer = datetime.timedelta(seconds = total_seconds)
        print(timer, end="\r")
        time.sleep(1)
        total_seconds -= 1
 
    print("Bzzzt! The countdown is at zero seconds!")

m = input("Enter the time in minutes: ")
s = input("Enter the time in seconds: ")
countdown(int(m), int(s))