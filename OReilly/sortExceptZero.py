from typing import Iterable


def except_zero(items: list) -> Iterable:
    
    zeropos = []
    for x in range(len(items)):
        if items[x] == 0:
            zeropos.append(x)
    #remove all zeros starting from end of list.
    zeropos.reverse()
    for z in zeropos:
        items.pop(z)

    #sort the list now that the zeros have been temporarily removed.
    items.sort()

    #add the zeros back into their original positions.
    zeropos.reverse()
    for z in zeropos:
        items.insert(z, 0)

    return items


if __name__ == '__main__':
    print("Example:")
    print(list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])) == [1, 3, 0, 0, 4, 4, 5, 0, 7]
    assert list(except_zero([0, 2, 3, 1, 0, 4, 5])) == [0, 1, 2, 3, 0, 4, 5]
    assert list(except_zero([0, 0, 0, 1, 0])) == [0, 0, 0, 1, 0]
    assert list(except_zero([4, 5, 3, 1, 1])) == [1, 1, 3, 4, 5]
    assert list(except_zero([0, 0])) == [0, 0]
    print("Coding complete? Click 'Check' to earn cool rewards!")
