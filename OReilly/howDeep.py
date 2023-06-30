import math

#ascertain the maximum depth of items in this layer. If item is a tuple then recursion is used.
def explore_tuple(structure, depth):
    l = [explore_tuple(x, depth + 1) for x in structure if isinstance(x,tuple)]
    #return max(l) if len(l) > 0 else depth
    #Alternative use max default keyword parameter.
    return max(l, default=depth)

def how_deep(structure):
    #use recursive function to explore a tuple - starting at a depth of 1.
    return explore_tuple(structure, 1)

if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for an auto-testing
    assert how_deep((1, 2, 3)) == 1
    assert how_deep((1, 2, (3,))) == 2
    assert how_deep((1, 2, (3, (4,)))) == 3
    assert how_deep(()) == 1
    assert how_deep(((),)) == 2
    assert how_deep((((),),)) == 3
    assert how_deep((1, (2,), (3,))) == 2
    assert how_deep((1, ((),), (3,))) == 3
    print("Coding complete? Click 'Check' to earn cool rewards!")
