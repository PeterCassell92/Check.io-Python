def flat_list(array):
	#approach 1
	flat = []
	for x in array:
		flat += flat_list(x) if type(x) is list else [x]
	return flat

	#approach 2. Unpacking lists not viable with list comprehension like this
	# return [x for x in array if type(x) is not list else flat_list(x)]

	#actually it is possible using the sum function like so. Smart solution.
	# Random Review (?)
	# u = lambda x: [x] if isinstance(x, int) else flat_list(x)
	# flat_list = lambda a: sum([u(i) for i in a], [])

if __name__ == '__main__':
	assert flat_list([1, 2, 3]) == [1, 2, 3], "First"
	assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "Second"
	assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "Third"
	assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "Four"
	print('Done! Check it')