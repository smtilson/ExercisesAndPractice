from datetime import datetime, date, timedelta
import os
import urllib.request


SHUTDOWN_EVENT = 'Shutdown initiated'



def convert_to_datetime(line):
    first_pass = line.split()
    second_pass = first_pass[1].split('T')
    date_data = list(map(int,second_pass[0].split('-')))
    time_data = list(map(int,second_pass[1].split(':')))
    return datetime(year= date_data[0], month= date_data[1], day= date_data[2],
                    hour=time_data[0], minute=time_data[1], second= time_data[2])


def time_between_shutdowns(loglines):
    times = []
    for line in loglines:
        if SHUTDOWN_EVENT in line:
            times.append(convert_to_datetime(line))
        else:
            continue
    return times[-1] - times[0]

start_100days = date(2017, 3, 30)
pybites_founded = date(2016, 12, 19)
pycon_date = date(2018, 5, 8)


def get_hundred_days_end_date():
    end_100days = start_100days+timedelta(days=100)
    print(end_100days.isoformat())
    return end_100days.isoformat()


def get_days_between_pb_start_first_joint_pycon():
    diff = pycon_date-pybites_founded
    print(diff.days)
    return diff.days

THIS_YEAR = 2018


def years_ago(date):
    new_date = datetime.strptime(date, '%d %b, %Y')
    print(int(THIS_YEAR - new_date.year))
    return int(THIS_YEAR - new_date.year)

years_ago("8 Aug, 2015")

def convert_eu_to_us_date(date):
    actual_date = datetime.strptime(date, '%d/%m/%Y')
    return actual_date.strftime('%m/%d/%Y')