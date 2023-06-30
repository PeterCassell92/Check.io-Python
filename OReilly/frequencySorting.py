def reverse_ascending(items):
    #split the lists into asc desc groups
    l = []
    grad = None
    g = []
    for i, item in enumerate(items):
        if i < len(items) -1:
            s =(items[i+1] - item > 0)
            if  grad == s:
                g.append(item)
            elif grad is None:
                g.append(item)
                grad = s
            else:
                #if positive gradient then add item then reverse list and extend l.
                if grad:
                    g.append(item)
                    g.reverse()
                    l.extend(g)
                    g=[] # alternative g.clear()
                #else if negative gradient then extend l and add item to new list.
                else:
                    l.extend(g)
                    g=[item]
                #change gradient
                grad = not grad
        else:
            g.append(item)
    if len(g) > 0:
        if grad:
            g.reverse()
        l.extend(g)
    return l


if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(reverse_ascending([1, 2, 3, 4, 5])) == [5, 4, 3, 2, 1]
    assert list(reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3])) == [10, 7, 5, 4, 8, 7, 2, 3, 1]
    assert list(reverse_ascending([5, 4, 3, 2, 1])) == [5, 4, 3, 2, 1]
    assert list(reverse_ascending([])) == []
    assert list(reverse_ascending([1])) == [1]
    assert list(reverse_ascending([1, 1])) == [1, 1]
    assert list(reverse_ascending([1, 1, 2])) == [1, 2, 1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
