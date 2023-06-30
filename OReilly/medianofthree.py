from typing import Iterable, List

def get_median(data: List[int]) -> [int, float]:
	data.sort(key= lambda x: x)
	return data[int(len(data)/2)] if len(data) % 2 != 0 else data[int(len(data)/2)-1] + (data[int(len(data)/2)] - data[int(len(data)/2)-1])/2


def median_three(els: Iterable[int]) -> Iterable[int]:
	
	if len(els) < 3:
		return els
	else:
		median_list = [get_median([els[i-2],els[i-1],x]) for i,x in enumerate(els) if i > 1]
		return els[0:2]+median_list


if __name__ == '__main__':
	print("Example:")
	print(list(median_three([1, 2, 3, 4, 5, 6, 7])))
	
	# These "asserts" are used for self-checking and not for an auto-testing
	assert list(median_three([1, 2, 3, 4, 5, 6, 7])) == [1, 2, 2, 3, 4, 5, 6]
	assert list(median_three([1])) == [1]
	print("Coding complete? Click 'Check' to earn cool rewards!")
