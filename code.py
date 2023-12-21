for row in range(10):
	for column in range(5):
		print('<' if row % 2 == 1 else '>', end='  ')
	print()	