import re

def is_stressful(subj):
    #method 1 - regex strings made manually
    #return True if subj.upper() == subj or re.search("!!!$",subj) or re.search("[hH].*[eE].*[lL].*[pP].*", subj) or re.search("[aA].*[sS].*[aA].*[pP].*", subj) or re.search("[uU].*[rR].*[gG].*[eE].*[nN].*[tT].*", subj) else False

    # method 2 - similar regex strings can be made and executed iteratively
    #keywords that can be found anywhere and with any number of repeat or inbetween characters
    keywords = ["help", "asap", "urgent"]
    keywordRegStr = lambda word: "".join(["["+ char + char.upper()+ "]+" + "[^a-zA-Z0-9\s]*" for char in word])
    regexStrings= [keywordRegStr(word) for word in keywords] + ["!!!$"]
    #print(regexStrings)
    return True if (subj.upper() == subj) or any(re.search(regStr,subj) for regStr in regexStrings) else False
    
if __name__ == '__main__':
    #These "asserts" are only for self-checking and not necessarily for auto-testing
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"
    print('Done! Go Check it!')


