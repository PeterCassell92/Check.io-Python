def sun_angle(time):
    #method 1
    s = time.split(':')
    #get mins elapsed in day and remove 6 hours as this is the zero point of our linear function
    mins = int(s[0])*60 + int(s[1]) - 6*60
    #if within bounds return percentage of daytime elapsed scaled by 180
    return round((mins/upper)*180,2) if (upper :=12*60) >= mins >= 0 else "I don't see the sun!"





if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
