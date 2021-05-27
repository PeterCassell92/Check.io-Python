import datetime as dt

def date_time(time: str) -> str:
    #method 1
    months = {
    	'01': 'January',
    	'02': 'February',
    	'03': 'March',
    	'04': 'April',
    	'05': 'May',
    	'06': 'June',
    	'07': 'July',
    	'08': 'August',
    	'09': 'September',
    	'10': 'October',
    	'11': 'November',
    	'12': 'December'
    }

    d, t = (s := time.split())[0].split('.'), s[1].split(':')
    return ' '.join([stripLeadingZero(d[0]), months[d[1]], d[2], "year", stripLeadingZero(t[0]),  pluralize(t[0],"hour"), stripLeadingZero(t[1]), pluralize(t[1],"minute")])

def stripLeadingZero(text: str):
	return text[1:] if text[0] == '0' else text

def pluralize(num: str, unit: str):
	return unit + "s" if int(num) != 1 else unit


if __name__ == '__main__':
    print("Example:")
    print(date_time('01.01.2000 00:00'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes", "Millenium"
    assert date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory"
    assert date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
    print("Coding complete? Click 'Check' to earn cool rewards!")
