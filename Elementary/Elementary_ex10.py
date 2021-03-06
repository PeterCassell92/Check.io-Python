def max_digit(number: int) -> int:
    # method 1
    # digits = [int(x) for x in str(number)]
    # digits.sort(reverse=True) #sort modifies original list but only returns None   
    # return digits[0]

    #method 2 more concise - using sorted function for one liner
    return sorted([int(x) for x in str(number)] ,reverse=True)[0]


if __name__ == '__main__':
    print("Example:")
    print(max_digit(0))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert max_digit(0) == 0
    assert max_digit(52) == 5
    assert max_digit(634) == 6
    assert max_digit(1) == 1
    assert max_digit(10000) == 1
    print("Coding complete? Click 'Check' to earn cool rewards!")
