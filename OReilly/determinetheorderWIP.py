def addToOrder(order, new, offset):
    [n for n in new if n not in order]

def splitStrToChar(s):
    return [char for char in s]

def generateOrderStructureFromData(order, data):
    for x in data:
        for i, char in enumerate(x):
            # print(char)
            if char in order:
               order[char]["goesBefore"] += "".join(filter(lambda y: y not in order[char]["goesBefore"], list(x[i+1:])))
               order[char]["goesAfter"] += "".join(filter(lambda y: y not in order[char]["goesAfter"], list(x[:i])))  
            else:
                order[char] = {
                    "goesBefore": x[i+1:],
                    "goesAfter": x[:i]
                }

     #Complete the order structure by cross-referencing
    for letter in order.keys():
        if (len(order[letter]["goesBefore"]) + len(order[letter]["goesAfter"])) != (len(order.keys())-1):            
            for x in order[letter]["goesBefore"]:
                order[letter]["goesBefore"] += "".join(filter(lambda k: k not in order[letter]["goesBefore"] and k !=letter, splitStrToChar(order[x]["goesBefore"])))
            for y in order[letter]["goesAfter"]:
                order[letter]["goesAfter"] += "".join(filter(lambda l: l not in order[letter]["goesAfter"] and l !=letter, splitStrToChar(order[y]["goesAfter"])))
    return order

def checkio(data):
    order = generateOrderStructureFromData({}, data)
    arr = sorted([l for l in order.keys()], reverse=True)
    val = None
    for letter in arr:
        print(letter)
        print(order[letter])

    val = sorted(arr, key=lambda x: len(order[x]["goesBefore"]))
    val.reverse()
    print(val)
    return "".join(val)

    if len(order.keys()) == len(set([len(order[x]["goesBefore"]) for x in order.keys()])):
        val = "".join(sorted(arr, key=lambda x: len(order[x]["goesBefore"]), reverse = True))
    else:
        val = "".join(sorted(arr))
    print(val)
    return val
    arr = []
    fail = False

    for letter in order.keys():
        print(letter)
        print(order[letter])
        if len(arr) == 0 or fail:
            arr.append(letter)
        else:
            #for each other letter in order, flesh out the goes before and goes after
            #i.e. take each letter in the goesBefore and access the attribute of order to get further info from that item.
            #find index where all goesAfter elements precede it and all goesBefore elements follow i
            if goesBefore:= next(filter(lambda y: y in order[letter]["goesBefore"], arr), None):
                arr.insert(arr.index(goesBefore), letter)
            elif goesAfter:= next(reversed(list(filter(lambda y: y in order[letter]["goesAfter"], arr))), None):
                arr.insert(arr.index(goesAfter)+1, letter)
            else:
                #entire list will now be sorted by english dict as one (or more) letters have insufficient info.
                fail = True
                arr.append(letter)

    val = "".join(arr) if not fail else "".join(sorted(arr))
    print(val)
    return val

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(["acb", "bd", "zwa"]) == "zwacbd", \
        "Just concatenate it"
    assert checkio(["klm", "kadl", "lsm"]) == "kadlsm", \
        "Paste in"
    assert checkio(["a", "b", "c"]) == "abc", \
        "Cant determine the order - use english alphabet"
    assert checkio(["aazzss"]) == "azs", \
        "Each symbol only once"
    assert checkio(["jhgfdba","jihcba","jigedca"]) == "jihgefdcba", \
        "from test case"