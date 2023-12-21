def highest_checker(p, q, r):
	largest = 0

	if p > q and p > r:
		largest = p

	elif q > p and q > r:
		largest = q

	elif r > q and r > p:
		largest = r


	return f"The highest is {largest}"

print(highest_checker(5, 4, 8))