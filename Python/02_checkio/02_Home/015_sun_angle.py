# Sun Angle

# Every true traveler must know how to do 3 things: fix the fire, find the 
# water and extract useful information from the nature around him. Programming 
# won't help you with the fire and water, but when it comes to the information 
# extraction - it might be just the thing you need.

# Your task is to find the angle of the sun above the horizon knowing the time 
# of the day. Input data: the sun rises in the East at 6:00 AM, which 
# corresponds to the angle of 0 degrees. At 12:00 PM the sun reaches its 
# zenith, which means that the angle equals 90 degrees. 6:00 PM is the time of 
# the sunset so the angle is 180 degrees. If the input will be the time of the 
# night (before 6:00 AM or after 6:00 PM), your function should return - "I 
# don't see the sun!".

# Input: The time of the day.
# Output: The angle of the sun, rounded to 2 decimal places.

# Example:
# sun_angle("07:00") == 15
# sun_angle("12:15") == 93.75
# sun_angle("01:23") == "I don't see the sun!"

from typing import Union
import datetime

def sun_angle(time: str) -> Union[int, str]:
    const = 0.25 # deg per minute
    deny = "I don't see the sun!"
    h, m = str(time).split(':')
    f_time = datetime.time(int(h),int(m))
    if datetime.time(int(6),int(0)) <= f_time <= datetime.time(int(18),int(0)) :
        return const * ((int(h)-6) * 60 + int(m))
    else :
        return deny


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
