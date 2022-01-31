# Date and Time Converter

# Computer date and time format consists only of numbers, for example: 
# 21.05.2018 16:30
# Humans prefer to see something like this: 
# 21 May 2018 year, 16 hours 30 minutes
# Your task is simple - convert the input date and time from computer format 
# into a "human" format.

# Input: Date and time as a string
# Output: The same date and time, but in a more readable format

# Example:

# date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes"
# date_time("19.09.2999 01:59") == "19 September 2999 year 1 hour 59 minutes"
# date_time("21.10.1999 18:01") == "21 October 1999 year 18 hours 1 minute"

# NB: words "hour" and "minute" are to be used only when time is 01:mm (1 hour) 
# or hh:01 (1 minute).
# In other cases "hours" and "minutes" should be used.

# How it is used: To improve the understanding between computers and humans.

# Precondition :
# 0 < day <= 31
# 0 < month <= 12
# 0 < year <= 3000
# 0 <= hours < 24
# 0 <= minutes < 60
import datetime
from posixpath import split

# first solution (just start typing immediately). Btw not so fast .-.
def date_time(time: str) -> str:
    date_1 = time.split(' ')
    dmy = date_1[0].split('.')
    hms = date_1[1].split(':')
    format_in = "%d.%m.%Y %H:%M"
    hrs_w = 'hour' if int(hms[0]) == 1 else 'hours'
    mnt_w = 'minute' if int(hms[1]) == 1 else 'minutes'
    my_date = datetime.datetime.strptime(time, format_in)
    return ' '.join([str(int(dmy[0])), str(my_date.strftime('%B')), str(dmy[2]), 'year', str(int(hms[0])), hrs_w, str(int(hms[1])), mnt_w]) 

if __name__ == "__main__":
    print("Example:")
    print(date_time("01.01.2000 00:00"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert (
        date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes"
    ), "Millenium"
    assert (
        date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes"
    ), "Victory"
    assert (
        date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes"
    ), "Somebody was born"
    print("Coding complete? Click 'Check' to earn cool rewards!")
