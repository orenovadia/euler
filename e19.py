from datetime import datetime, timedelta

if __name__ == '__main__':
    start = datetime(1901, 1, 1)
    stop = datetime(2000, 12, 31)
    start.weekday()
    sundays = 0
    while start <= stop:
        if start.weekday() == 6 and start.day == 1:
            sundays += 1
        start += timedelta(days=1)
    print (sundays)