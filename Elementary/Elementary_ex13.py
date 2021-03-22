def nearest_value(values: set, one: int) -> int:
    # method one
    l = list(values)
    output = None
    #if one is in list then output one
    if(one in l):
        output = one
    #else find closest neighbour
    else:
        #add value and sort list ascending
        l.append(one)
        l.sort()
        i = l.index(one)
        #get differences between value and neighbours if neighbour exists
        diff1 = one - l[i-1] if i - 1 >=0 else None
        diff2 = l[i+1]-one if i + 1 < len(l) else None   

        #compare diffs and return closest neighbour
        if (diff1 != None and diff2 == None) or (diff1 != None and diff2!=None and diff1 <= diff2):
            output =  l[i-1]
        elif (diff2 != None and diff1 == None) or (diff2 != None and diff1 !=None and diff2 < diff1):
            output =  l[i+1]
    return output


if __name__ == '__main__':
    print("Example:")
    #print(nearest_value({4, 7, 10, 11, 12, 17}, 9))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
    assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
    assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
    assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
    assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
    assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
    assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
    assert nearest_value({-1, 2, 3}, 0) == -1
    print("Coding complete? Click 'Check' to earn cool rewards!")
