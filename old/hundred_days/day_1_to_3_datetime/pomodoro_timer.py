from datetime import datetime, timedelta





def run_pomodoro(duration, count):
    print(f"You are now beginning a work session which is {duration} minutes long.")
    current_time = datetime.now()

    end_time = current_time + timedelta(minutes=duration)
    while current_time< end_time:
        current_time = datetime.now()
        if end_time - current_time-timedelta(minutes=5) == timedelta(seconds=1):
            print("5 minutes left.")
        elif end_time - current_time-timedelta(minutes=1) == timedelta(seconds=1):
            print("1 minutes left.")
        else:
            continue
    count+=1
    print(f"You have now completeed {count} pomodoro's.")
    return count

def run_break(duration):
    print(f"Your {duration} minute break has begun.")
    current_time = datetime.now()

    end_time = current_time + timedelta(minutes=duration)
    while current_time < end_time:
        current_time = datetime.now()
        if end_time - current_time-timedelta(seconds=30) == timedelta(seconds=1):
            print("30 seconds left.")
        else:
            continue
    print("Your break is done, time to get back to work.")

def run_method():
    length = int(input("How many minutes should each session be?"))

    break_time = int(input("How many minutes should each break be?"))

    pomodoro_count = 0
    val = 1
    while val == 1:
        pomodoro_count = run_pomodoro(length, pomodoro_count)
        asd = input("Enter something to begin your break.")
        run_break(break_time)
        val = int(input('Enter 1 if you want to continue with another pomodoro?'))
    print(f"Finished, you did {pomodoro_count} pomodoros.")
run_method()