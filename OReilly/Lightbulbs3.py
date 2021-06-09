#  In the third mission from the series about lightbulbs, I want to separately highlight the process and the period of observation of this process.

# In the previous mission, the start_watching parameter was introduced, and in this one - the end_watching parameter, which tells the time when it’s necessary to end the observation. If it’s not passed, the mission works as in the previous version, with no observation time limit.

# One more update is that the amount of elements (button clicks) can be odd (previously there was a precondition, that the amount of elements is always even). 

from datetime import datetime
from typing import List, Optional

def sum_light(els: List[datetime], start_watching: Optional[datetime] = datetime(year=1970, month=1,day=1), end_watching: Optional[datetime] = datetime(year=9999, month=12, day=31)) -> int:
    """
        how long the light bulb has been turned on
    """
    #if list is not even then add end watching as final dt.
    if len(els) %2 != 0:
    	els.append(end_watching)

    mins_counted = 0
    #iterate through each pair in the list. These periods represent times when the lightbulb is on.
    #If any of the period is included in watched period, then add this time to mins_counted
    for i in range(1,len(els),2):
    	#get the period's end and start times, accounting for whether the start or end watching times fall within the period.
    	end = els[i] if els[i] < end_watching else end_watching
    	start = els[i-1] if els[i-1] > start_watching else start_watching
    	#get the total second elapsed between start and end unless the entire period is not within the watched period.
    	mins_counted += int((end-start).total_seconds()) if els[i] > start_watching and els[i-1] < end_watching else 0   

    return mins_counted 


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
    start_watching=datetime(2015, 1, 12, 10, 0, 0),
    end_watching=datetime(2015, 1, 12, 10, 0, 10)) == 10
    
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