def number_length(a: int) -> int:
    # your code here
    #return len(str(a)) #bool() float() int()
    if(a):
        x = 0
        while a >= 1:
            a = a /10
            x += 1
        return x
    else:
        return 1
    


if __name__ == '__main__':
    print("Example:")
    print(number_length(10))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert number_length(10) == 2
    assert number_length(0) == 1
    assert number_length(4) == 1
    assert number_length(44) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")
