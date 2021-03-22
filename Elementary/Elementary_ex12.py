def beginning_zeros(number: str) -> int:
    # method 1
    # i=0
    # for x in number:
    #     if x =='0':
    #         i+=1
    #     else:
    #         return i
    # return i

    #method 2 - single line expression
    #gets the index of the first digit that is not 0. If there are no digits that aren't 0 then returns length of whole string.
    return number.index(next(iter(s))) if not len(s:=[x for x in number if x != '0']) ==0 else len(number)
    #using iter() to turn list into iterable as they have different behaviours.


if __name__ == '__main__':
    print("Example:")
   # print(beginning_zeros('100'))

    # These "asserts" are used for self-checking and not for an auto-testing
    print(beginning_zeros('100'))
    print(beginning_zeros('001') )
    print(beginning_zeros('100100'))
    print(beginning_zeros('001001') )
    print(beginning_zeros('012345679') )
    print(beginning_zeros('0000'))
    print("Coding complete? Click 'Check' to earn cool rewards!")

    # These "asserts" are used for self-checking and not for an auto-testing
    assert beginning_zeros('100') == 0
    assert beginning_zeros('001') == 2
    assert beginning_zeros('100100') == 0
    assert beginning_zeros('001001') == 2
    assert beginning_zeros('012345679') == 1
    assert beginning_zeros('0000') == 4
    print("Coding complete? Click 'Check' to earn cool rewards!")
