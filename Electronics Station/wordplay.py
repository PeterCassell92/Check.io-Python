import re

def check_char_match(direction, pos, text, word, char_index):
	nextx = direction[0]+pos[0]
	nexty = direction[1]+pos[1]
	if text[nextx] and len(text[nextx])>nexty and text[nextx][nexty] == word[char_index]:
		if char_index == len(word)-1:
			return [nextx+1, nexty+1]
		else:
			return check_char_match(direction, (nextx, nexty), text, word, char_index+1)
	else:
		return False

def checkio(text, word):

	text = re.sub(r'[^\n\S\w]', '', text.lower()).split('\n')

	#get all start positions as tuples (row, column)
	start_positions = []
	i=0
	for x in text:
		matches = re.finditer(word[0], x)
		if matches:
			for item in matches:
				 start_positions.append((i ,item.span()[0]))
		i +=1

	#check each cardinal direction for next character match in keyword 
	directions = [(1,0), (0,1), (-1,0), (0,-1)]
	for pos in start_positions:
		for drc in directions:
			if result := check_char_match(drc, pos, text, word, 1):
				return [pos[0]+1, pos[1]+1] +result


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("""DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?""", "ten") == [2, 14, 2, 16]
    assert checkio("""He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!""", "noir") == [4, 16, 7, 16]
print("Coding complete? Click 'Check' to earn cool rewards!")


