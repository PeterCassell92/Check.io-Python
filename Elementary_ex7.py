from typing import Iterable


def remove_all_before(items: list, border: int) -> Iterable:
    # method 1
    # o = lambda items, i: items[i:]
    # try:
    #     i = items.index(border)
    #     return o(items, i)
    # except ValueError:
    #     return items

    # method 2 - more concise and not using try except
    return items[items.index(border):] if border in items else items

    #method 3 - one line but using try except
    #no option to condense try except to one line python


if __name__ == '__main__':
    print("Example:")
    #print(list(remove_all_before([1, 2, 3, 4, 5], 3)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(remove_all_before([1, 2, 3, 4, 5], 3)) == [3, 4, 5]
    assert list(remove_all_before([1, 1, 2, 2, 3, 3], 2)) == [2, 2, 3, 3]
    assert list(remove_all_before([1, 1, 2, 4, 2, 3, 4], 2)) == [2, 4, 2, 3, 4]
    assert list(remove_all_before([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]
    assert list(remove_all_before([], 0)) == []
    assert list(remove_all_before([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)) == [7, 7, 7, 7, 7, 7, 7, 7, 7]
    print("Coding complete? Click 'Check' to earn cool rewards!")
