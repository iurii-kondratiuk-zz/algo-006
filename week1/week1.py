def _SortAndCountInversions(arr, start, end):
	if (start == end):
		return 0
	else:
		x = _SortAndCountInversions(arr, start, (end + start) / 2)
		y = _SortAndCountInversions(arr, (end + start) / 2 + 1, end)
		z = _MergeAndCountSplitInversions(arr, start, (end + start) / 2 + 1, end)
		return (x + y + z)

def _MergeAndCountSplitInversions(arr, start, middle, end):
	inv = 0
	i = start
	j = middle
	res = []

	while (i < middle or j <= end):
		if (i == middle):
			res.append(arr[j])
			j += 1	
		elif (j > end):
			res.append(arr[i])
			i += 1
		elif (arr[i] <= arr[j]):
			res.append(arr[i])
			i += 1
		else:
			res.append(arr[j])
			j += 1
			inv += (middle - i)

	i = start
	while (i <= end):
		arr[i] = res[i - start]
		i += 1

	return inv

def CountInversions(arr):
	return _SortAndCountInversions(arr, 0, len(arr) - 1)

def main():
    with open('IntegerArray.txt') as f:
        data =  [int(x) for x in f]
    
    print(CountInversions(data))

if __name__ == '__main__':
    main()

