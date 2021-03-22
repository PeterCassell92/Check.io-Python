def split_pairs(a):
    # method 1
    # l = []
    # for x in range(0,len(a),2):
    #     l.append(s if len(s := a[x:x+2]) ==2 else a[x]+"_") #using python 3.8 walrus operator for the first time. it's neat
    # return l

    #method 2 using list comprehension to make more concise
    #[x for x in fruits if "a" in x] - list comprehension syntax with condition as filter
   
    return [s if len(s:= a[x:x+2]) == 2 else a[x]+"_" for x in range(0,len(a),2)]


if __name__ == '__main__':
    print("Example:")
    print(list(split_pairs('abcd')))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(split_pairs('abcd')) == ['ab', 'cd']
    assert list(split_pairs('abc')) == ['ab', 'c_']
    assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    assert list(split_pairs('a')) == ['a_']
    assert list(split_pairs('')) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
