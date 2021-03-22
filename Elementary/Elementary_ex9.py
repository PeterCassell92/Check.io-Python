from typing import Iterable


def replace_first(items: list) -> Iterable:
    # your code here
    # method 1
    # if len(items) > 1:
    # 	items.append(items[0])
    # 	return items[1:]
    # return items

    #method 2 concise 
    return items[1:] if len(items) > 1 and items.append(items[0]) is None else items

    #method 3 concise and neater (without second hacky expression) - taken from solutions
    #i'd forgotten in python that you can do list concatenations like this
    #return items[1:] + items[0:1] if len(items) > 1 else items

if __name__ == '__main__':
    print("Example:")
    print(list(replace_first([1, 2, 3, 4])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(replace_first([1, 2, 3, 4])) == [2, 3, 4, 1]
    assert list(replace_first([1])) == [1]
    assert list(replace_first([])) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
