evenNumber = 0
oddNumber  = 0

for number in range(1, 101):
	if number % 2  == 0:
		evenNumber += 1
	else:
		oddNumber += 1

print("the number of even number is", evenNumber)

print("the number of odd number is", oddNumber)

