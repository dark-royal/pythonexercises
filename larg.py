count = 0

array = [23, 45, 21, 98]

largest = array[0]

for item in array:
	if item > largest:
		largest = item
		print(largest)