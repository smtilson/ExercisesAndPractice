import datetime

start = datetime.datetime.now()
increment = input("Please enter an increment such as weeks, days, hours, minutes, or seconds.")
length = input("Please enter how many of them before the timer goes off.")
difference = eval("datetime.timedelta("+increment+" = "+length+")")
end = start+difference
current_time= start
counter = 0
tick = datetime.timedelta(seconds=5)
while current_time< end:
    current_time = datetime.datetime.now()
    if start+tick - current_time<datetime.timedelta(seconds=1):
        print("5 seconds has passed.")
        tick += datetime.timedelta(seconds=5)
        counter+=1
    else:
        continue

print("the timer is finished")
print(f"the clock ticked {counter} times")