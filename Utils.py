from datetime import datetime


def StrToTimeFrame(StartTime, EndTime):
    datetime_start = datetime.strptime(StartTime, '%Y-%m-%d %H:%M:%S')
    datetime_end = datetime.strptime(EndTime, '%Y-%m-%d %H:%M:%S')
    diff = datetime_end - datetime_start
    print(diff.total_seconds())
