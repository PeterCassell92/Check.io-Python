#  This is the second mission in the lightbulb series.
#I will try to make each following task slightly more complex.

# You have already learned how to count the amount of time a light bulb has been on,
#or how long a room has been lit. Now let's add one more parameter - the counting start time.

# This means that the light continues to turn on and off as before.
#But now, as a result of the function, I want not only to know how long
#there was light in the room, but how long the room was lit, starting from a
#certain moment.

# One more argument is added – start_watching , and if it’s not passed,
#we count as in the previous version of the program for the entire period. 

# Taken from mission Lightbulb Intro

# With this mission I want to start a series of missions with light bulbs.
#They will help you understand the concept of processes and evaluation of the
#processes’ performance. Instead of light bulbs, in real life,
#there may be equipment, the effectiveness of which must be calculated, or workers who go to work, and their wages must be calculated.

# The first mission is quite simple. There is a light bulb, which by default is off,
# and a button, by pressing which the light bulb switches its state.
#This means that if the light bulb is off and the button is pressed,
#the light turns on, and if you press it again, it turns off.

from datetime import datetime
from typing import List, Optional

def sum_light(els: List[datetime], start_watching: Optional[datetime] = None) -> int:
    """
        how long the light bulb has been turned on
    """#
    difs = list(map(lambda i: int((els[i] -(start_watching if start_watching and start_watching > els[i-1] else els[i-1])).total_seconds()) if not start_watching or start_watching <= els[i] else 0 , [*range(1,len(els),2)]))
    print(difs)
    return sum(difs)

if __name__ == '__main__':
    print("Example:")
    print(sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 10),
    ],
    datetime(2015, 1, 12, 10, 0, 5)))
    
    assert sum_light(els=[
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 10),
    ],
    start_watching=datetime(2015, 1, 12, 10, 0, 5)) == 5
    

    
    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 10),
    ], datetime(2015, 1, 12, 10, 0, 0)) == 10
    
    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
    ], datetime(2015, 1, 12, 11, 0, 0)) == 610
    
    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
    ], datetime(2015, 1, 12, 11, 0, 10)) == 600
    
    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
    ], datetime(2015, 1, 12, 10, 10, 0)) == 620

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
        datetime(2015, 1, 12, 11, 10, 11),
        datetime(2015, 1, 12, 12, 10, 11),
    ], datetime(2015, 1, 12, 12, 10, 11)) == 0

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
        datetime(2015, 1, 12, 11, 10, 11),
        datetime(2015, 1, 12, 12, 10, 11),
    ], datetime(2015, 1, 12, 12, 9, 11)) == 60
    
    print("The second mission in series is done? Click 'Check' to earn cool rewards!")