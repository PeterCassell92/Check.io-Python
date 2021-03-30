def split_list(items: list) -> list:
    # method 1
    # num =  int(len(items)/2) if len(items) %2==0 else round(len(items)/2 + 0.5)
    # return [items[:num], items[num:]]

    # method 2 - saw in solutions afterwards but was neat and introduced me to divide without remainder //
    num =  len(items)//2 + len(items)%2
    return [items[:num], items[num:]]


if __name__ == '__main__':
    print("Example:")
    print(split_list([1, 2, 3, 4, 5, 6]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert split_list([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]
    assert split_list([1, 2, 3]) == [[1, 2], [3]]
    assert split_list([1, 2, 3, 4, 5]) == [[1, 2, 3], [4, 5]]
    assert split_list([1]) == [[1], []]
    assert split_list([]) == [[], []]
    print("Coding complete? Click 'Check' to earn cool rewards!")
