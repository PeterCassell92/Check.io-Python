def safe_pawns(pawns: set) -> int:
	#pawns have the following moveset
	moveset = {(-1,1),(1,1)}
	#for each move available to the piece, find the line of sight of that move
	targetedSquares = {getMoveTargetSquare(position,move) for position in pawns for move in moveset}
	#find which pawn positions are in the pawn list. Use set comprehension to automatically de-dupe values.
	#this is example of where set comprehension makes code simpler than list comprehension
	safe = {x for x in targetedSquares if (any(x == position for position in pawns))}
	return len(safe)

#takes position (string) and move (tuple) and returns the position of the targeted square
getMoveTargetSquare = lambda pos, move: chr(ord(pos[0]) + move[0]) + str(int(pos[1]) + move[1])

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")