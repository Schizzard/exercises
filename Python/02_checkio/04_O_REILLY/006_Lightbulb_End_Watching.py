# Lightbulb End Watching

# In the third mission from the series about lightbulbs, I want to separately
# highlight the process and the period of observation of this process.

# In the previous mission, the start_watching parameter was introduced, and in
# this one - the end_watching parameter, which tells the time when it’s
# necessary to end the observation. If it’s not passed, the mission works as in
# the previous version, with no observation time limit.

# One more update is that the amount of elements (button clicks) can be odd
# (previously there was a precondition, that the amount of elements is always
# even).

# Input: Three arguments and only the first one is required. The first one is a
# list of datetime objects, the second and the third ones are the datetime
# objects.
# Output: A number of seconds as an integer.

# Example:
# sum_light([
#     datetime(2015, 1, 12, 10, 0, 0),
#     datetime(2015, 1, 12, 10, 10, 10),
#     datetime(2015, 1, 12, 11, 0, 0),
# ],
# datetime(2015, 1, 12, 10, 10, 0),
# datetime(2015, 1, 12, 11, 0, 10)) == 20

# sum_light([
#     datetime(2015, 1, 12, 10, 0, 0),
# ],
# datetime(2015, 1, 12, 9, 9, 0),
# datetime(2015, 1, 12, 10, 0, 0)) == 0

# sum_light([
#     datetime(2015, 1, 12, 10, 0, 0),
#     datetime(2015, 1, 12, 10, 10, 10),
#     datetime(2015, 1, 12, 11, 0, 0),
#     datetime(2015, 1, 12, 11, 10, 10),
# ],
# datetime(2015, 1, 12, 9, 0, 0),
# datetime(2015, 1, 12, 10, 5, 0)) == 300

# Precondition:
# The array of pressing the button is always sorted in ascending order.
# The array of pressing the button has no repeated elements.
# The minimum possible date is 1970-01-01
# The maximum possible date is 9999-12-31

from datetime import datetime
from re import S
from typing import List, Optional


# my solution
def sum_light(els: List[datetime], start_watching: Optional[datetime] = None, end_watching: Optional[datetime] = None) -> int:
    ans = []
    if len(els) % 2 != 0:
        els.append(datetime(9999, 1, 1, 0, 0, 0))

    if start_watching is None:
        start_watching = els[0]
    if end_watching is None:
        end_watching = els[-1]

    for start, end in zip(els[::2], els[1::2]):
        d1 = max(end, start_watching or end) - \
            max(start, start_watching or start)
        d2 = max(end, end_watching or end) - max(start, end_watching or start)
        ans.append(d1 - d2)
    return sum(i.total_seconds() for i in ans)


if __name__ == '__main__':
    print("Example:")
    print(sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 10),
    ],
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 10)))

    assert sum_light(els=[
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 10),
    ],
        st_w=datetime(2015, 1, 12, 10, 0, 0),
        end_w=datetime(2015, 1, 12, 10, 0, 10)) == 10

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 10),
    ],
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 7)) == 7

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 10),
    ],
        datetime(2015, 1, 12, 10, 0, 3),
        datetime(2015, 1, 12, 10, 0, 10)) == 7

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 10),
    ],
        datetime(2015, 1, 12, 10, 0, 10),
        datetime(2015, 1, 12, 10, 0, 20)) == 0

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
    ],
        datetime(2015, 1, 12, 10, 30, 0),
        datetime(2015, 1, 12, 11, 0, 0)) == 0

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
    ],
        datetime(2015, 1, 12, 10, 10, 0),
        datetime(2015, 1, 12, 11, 0, 0)) == 10

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
    ],
        datetime(2015, 1, 12, 10, 10, 0),
        datetime(2015, 1, 12, 11, 0, 10)) == 20

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
    ],
        datetime(2015, 1, 12, 9, 50, 0),
        datetime(2015, 1, 12, 10, 0, 10)) == 10

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
    ],
        datetime(2015, 1, 12, 9, 0, 0),
        datetime(2015, 1, 12, 10, 5, 0)) == 300

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
    ],
        datetime(2015, 1, 12, 11, 5, 0),
        datetime(2015, 1, 12, 12, 0, 0)) == 310

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
    ],
        datetime(2015, 1, 12, 11, 5, 0),
        datetime(2015, 1, 12, 11, 10, 0)) == 300

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
    ],
        datetime(2015, 1, 12, 10, 10, 0),
        datetime(2015, 1, 12, 11, 0, 10)) == 20

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
    ],
        datetime(2015, 1, 12, 9, 10, 0),
        datetime(2015, 1, 12, 10, 20, 20)) == 610

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
    ],
        datetime(2015, 1, 12, 9, 10, 0),
        datetime(2015, 1, 12, 10, 20, 20)) == 1220

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
    ],
        datetime(2015, 1, 12, 9, 9, 0),
        datetime(2015, 1, 12, 10, 0, 0)) == 0

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
    ],
        datetime(2015, 1, 12, 9, 9, 0),
        datetime(2015, 1, 12, 10, 0, 10)) == 10

    print("The third mission in series is completed? Click 'Check' to earn cool rewards!")
