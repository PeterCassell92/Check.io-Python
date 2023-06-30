def generateOrderStructureFromData(data):
    order = {}
    for x in data:
        for i, char in enumerate(x):
            # print(char)
            if char in order:
               order[char]["goesBefore"] += "".join(filter(lambda y: y not in order[char]["goesBefore"], list(x[i+1:]))) 
            else:
                order[char] = {
                    "goesBefore": x[i+1:],
                }

     #Complete the order structure by cross-referencing
    for letter in order.keys():           
        for x in order[letter]["goesBefore"]:
            order[letter]["goesBefore"] += "".join(filter(lambda k: k not in order[letter]["goesBefore"] and k !=letter, order[x]["goesBefore"]))
    return order

def checkio(data):
    order = generateOrderStructureFromData(data)
    arr = sorted([l for l in order.keys()])
    val = sorted(arr, key=lambda x: len(order[x]["goesBefore"]), reverse = True)
    return "".join(val)


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