count = 0
remainder = 0
number = int(input("Enter number,-1 to stop"))

while number != -1:
	number1 = number // 100
	remainder = number % 100

	print(number1,remainder)
	number = int(input("Enter number,-1 to stop"))
	
	
	count += 1


