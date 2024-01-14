def alternate_merge(list1, list2):

	if not list1:
		return list2

	if not  list2:
		return list1

	return [list1[0], list2[0]] + alternate_merge(list1[1:], list2[1:])

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

print(alternate_merge(list1, list2))