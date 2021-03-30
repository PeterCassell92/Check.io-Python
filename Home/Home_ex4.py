import re

def first_word(text: str) -> str:
    #method 1
    # word = ""
    # x = 0
    # while x < len(text) and (c := (text[x].isalpha() or text[x]=="'"))  or word == "":
    #     if c:
    #         word += text[x]
    #     x +=1
    # return word 
    return re.findall(r'\w+\'*\w*',text)[0]

if __name__ == '__main__':
    print("Example:")    
    first_word("'Hello")
    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
    print("Coding complete? Click 'Check' to earn cool rewards!")
