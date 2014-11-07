def _Swap(arr, i, j):
	temp = arr[i]
	arr[i] = arr[j]
	arr[j] = temp

def _isMedian(arr, i, j, k):
	return (arr[i] < arr[j] and arr[i] > arr[k]) or (arr[i] > arr[j] and arr[i] < arr[k])

def _QuickSort(arr, l, r, pivot):
	global comparisons

	if l >= r:
		return

	p = 0
	if pivot == 0:
		p = arr[l]
	elif pivot == 2:
		p = arr[r]
		_Swap(arr, l, r)
	elif pivot == 1:
		m = l + ((r-l) >> 1)
		if _isMedian(arr, l, m, r):
			p = arr[l]
		elif _isMedian(arr, m, l, r):
			p = arr[m]
			_Swap(arr, l, m)
		else:
			p = arr[r]
			_Swap(arr, l, r)

	comparisons += (r-l)

	i = l+1
	for j in range(i, r+1):
		if arr[j] < p:
			_Swap(arr, i, j)
			i += 1
	_Swap(arr, l, i-1)

	_QuickSort(arr, l, i-2, pivot)
	_QuickSort(arr, i, r, pivot)

def QuickSort(arr, pivot):
	_QuickSort(arr, 0, len(arr) - 1, pivot)

def main():
	with open('IntegerArray.txt') as f:
		data = [int(x) for x in f]

	global comparisons

	pivot = {
		'first': 0,
		'median': 1,
		'final': 2
	}
	
	comparisons = 0
	QuickSort(data[:], pivot['first'])
	print(comparisons)
	
	comparisons = 0
	QuickSort(data[:], pivot['median'])
	print(comparisons)
	
	comparisons = 0
	QuickSort(data[:], pivot['final'])
	print(comparisons)
	

if __name__ == '__main__':
	main()